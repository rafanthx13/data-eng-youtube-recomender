import datetime
import psycopg2
from env.load_env import *

class DataBase:

    TABLE_NAME = DB_TABLE

    def __init__(self):
        self.conn = self.connect_postgres()
        self.cur = self.conn.cursor()

    def connect_postgres(self):
        # connect to PostgreSQL
        print ("\nConnecting to PostgreSQL")
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME, user=DB_USER, password=DB_PASS,
                host=DB_HOST, port=DB_PORT
            )
        except Exception as err:
            print ("PostgreSQL Connect() ERROR:", err)
            conn = None
        # return the connection object
        return conn

    def create_table():
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id SERIAL primary key, 
                video_title TEXT, 
                video_link TEXT UNIQUE, 
                thumbnail TEXT, 
                score FLOAT, 
                liked BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT NOW(),
                updated_at DATE);
        """)
        self.conn.commit()

    def show_videos(self, qtd_videos = 20):
        """ Return list of videos for Front End """
        query = '''SELECT id, video_title, video_link, thumbnail, score, liked, created_at, upload_date FROM {TABLE_NAME}
                    ORDER BY score DESC LIMIT {qtd_videos}'''
        query = query.format(TABLE_NAME=self.TABLE_NAME, qtd_videos=qtd_videos)
        videos = self.execute_query(query)
        return videos if videos else []

    def execute_query(self, query, get_one=False):
        # psycogs fetch: list of tuples or tuple or None
        result = False
        self.cur.execute(query)
        if(result == None):
            return False
        return self.cur.fetchone() if get_one else self.cur.fetchall()
        
    def check_if_exist_video_link(self, video_link):
        """ Return one video by its link """
        query = '''SELECT * FROM {TABLE_NAME} WHERE video_link = '{video_link}' '''
        query = query.format(TABLE_NAME=self.TABLE_NAME, video_link=video_link)
        # print('=============', query)
        #   TTestar melhor essa parte
        ## https://pynative.com/python-postgresql-select-data-from-table/
        # print('execute query', query)
        video = self.execute_query(query, get_one=True)
        # print('resultado do video', video)
        if(not video):
            return False
        # print("**********************", video)
        return True


    def save_recomendation(self, video_info):
        # print(video_info)
        ''' check if video already exists '''
        video_title = video_info['title'].replace("'", '"')
        video_link = video_info['video_id']
        thumbnail = video_info['thumbnail']
        score = video_info['score']
        upload_date = str(video_info['upload_date'])
        print('upload_date ==', upload_date, '== upload_date')

        # Adicionar novas tabelas
        ## 1; Se for texto STRING, ponha entre aspas simples ';
        ## 2; insere na query e na linha de baixo, em 'INSERT INTO' e em 'query.format'
        query = '''
        INSERT INTO {TABLE_NAME} (video_title, video_link, thumbnail, score, upload_date) 
        VALUES ('{video_title}', '{video_link}', '{thumbnail}', {score}, '{upload_date}');
        '''
        query = query.format(TABLE_NAME=self.TABLE_NAME, video_link=video_link,
        thumbnail=thumbnail, score=score, video_title=video_title, upload_date=upload_date)
        self.cur.execute(query)
        self.conn.commit()
        count = self.cur.rowcount
        if(count == 0):
            print('NAO INSERIU', video_info['video_id'])
        
    #TALVEZ NEM VAI SUAR
    def like_video(self, liked_value, video_id):
        """" Edit liked column """
        update_time = datetime.datetime.now().strftime("%Y %m %d %H:%M:%S")


        query = '''update {TABLE_NAME} set liked = {liked_value},
                        updated_at = '{update_time}' where id = {video_id}
                '''
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()