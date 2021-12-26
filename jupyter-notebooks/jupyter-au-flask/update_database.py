

from extract_data import *
from ml_functions import *
from db import DataBase
import time
import os
import pandas as pd
from threading import Thread
from requests_html import HTMLSession
# from DAO.database import Database

from db import DataBase

queries = ['data+engineering', 'data+pipeline', "airflow"]


# Em suma: busca novos dados, aplica o modelo
def update_db():
    try:
        database = DataBase()
        for query in queries:
            
            for page in range(1,4):
                print(query, page)
                search_page = download_search_page(query, page)
                print("=========================")
                print(" *** search_page ***")
                print(search_page)
                print("=========================")
                video_list = parse_search_page(search_page)
                print("=========================")
                print(" *** video_list ***")
                print(video_list)
                print("=========================")
                df_videos = pd.DataFrame(video_list)
                
                for video in df_videos['link'].unique():
                    if database.get_by_link(video):
                        print("Already registered in database: {}".format(video))
                        continue
                    video_json_data = parse_video_page(video)
                    if(not video_json_data):
                        continue
                    
                    p = compute_prediction(video_json_data)

                    video_id = video
                    data_front = {
                        "title": video_json_data['title'],
                        "score": float(p),
                        "video_id": video_id,
                        "thumbnail": video_json_data['thumbnail']
                       }
                    data_front['update_time'] = time.time_ns()
                    print(video_id, json.dumps(data_front))
                    database.save_recomendation(data_front)
    except Exception as identifier:
        # os.remove("novos_videos.json")
        print("================", identifier)
        raise Exception('Internal Server Error')
    return True

    """
O que vai fazer:
 + Para cada query: 
  - Web Scraping
  - Buaca os dadoa de de uma pagina por query e por fim  os video
    - Buca novos videos desde que nao ja esstjam instalados 
      - é testtado com um select
      - si é permidido, o video é convertido
    - Com os dados no formato JSON faz a previsao

"""