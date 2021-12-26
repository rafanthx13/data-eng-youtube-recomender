

from extract_data import *
from ml_functions import *
from db import DataBase
import time
import os
import pandas as pd
from threading import Thread
from requests_html import HTMLSession
from db import DataBase

def check_if_not_exist_link(video_link, database):
    exist =  database.check_if_exist_video_link(video_link)
    if(exist):
        print("Already registered in database: {}".format(video_link))
        return False
    return True

def time_spent(time0):
    t = time.time() - time0
    t_int, t_min = int(t) // 60, t % 60
    return '{} min {:6.3f} s'.format(t_int, t_min) if t_int != 0 else '{:.3f} s'.format(t_min)

def print_debug(x, x_name):
    print()
    print('==========')
    print('****', x_name, '****')
    print(x)
    print('==========')
    print()

# app.route(/show-videos)
def get_all_videos():
    list_videos = []
    http_status = False
    try:
        database = DataBase()
        list_videos = database.show_videos()
        http_status = True
    except Exception as e:
        print('======\n\n', e, '\n\n========')
        raise Exception('Internal Server Error\n\n', e)
    finally:
        database.close()
        return list_videos, http_status


# @app.route('/update-db')
def update_db():
    t0 = time.time()
    http_status = False
    count_records = 0
    queries = ['data+engineering', 'data+pipeline', "airflow"]
    number_of_videos = 5
    try:
        database = DataBase()
        for query in queries:
            print(query, number_of_videos)
            # Busca 'number_of_videos' videos das paginas de search
            search_videos = download_search_page(query, number_of_videos)
            # Retira somente o id, a parte da URL que identifica o video
            id_videos = list(map(lambda v: v['id'], search_videos))
            print_debug(id_videos, 'id_videos')
            # Filtro video_id para nao repetir no banco e evitar loop de algo jja repetido
            new_id_videos = list(filter(
                lambda el: check_if_not_exist_link(el, database), id_videos ))
            if(new_id_videos == []):
                print('SEM VIDEOS')
                continue
            print_debug(new_id_videos, 'new_id_videos')
            # Para cade video novo
            for video in new_id_videos:
                # Busco seus dados
                video_data = download_video_page(video)
                # Calculo a probabilidade
                proba = compute_prediction(video_data)
                # Estruturo os dados para inserir no banco
                video_id = video
                data_front = {
                    "title": video_data['title'],
                    "score": float(proba),
                    "video_id": video_id,
                    "thumbnail": video_data['thumbnail'],
                    'update_time': time.time_ns()
                    }
                # Salvo no banco
                database.save_recomendation(data_front)
                count_records += 1
        http_status = True

    except Exception as e:
        print('======\n\n', e, '\n\n========')
        raise Exception('Internal Server Error\n\n', e)
        
    finally:
        database.close()
        return count_records, http_status, time_spent(t0)
