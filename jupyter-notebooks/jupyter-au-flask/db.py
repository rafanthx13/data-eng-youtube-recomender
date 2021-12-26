import datetime
import psycopg2
from config.env import *

class DataBase:

    TABLE_NAME = DB_TABLE

    def __init__(self):
        self.conn = self.connect_postgres()
        self.cur = self.conn.cursor()

    def connect_postgres(self):
        # connect to PostgreSQL
        print ("\nconnecting to PostgreSQL")
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
        self.close()   

    def show_videos(self, qtd_videos = 20):
        """ Return list of videos for Front End """
        query = '''select id, video_title, video_link, thumbnail, score, liked from {TABLE_NAME}
                    order by score desc limit {qtd_videos}'''
        videos = self.cur.execute(query)
        result = videos.fetchall()
        self.close() 
        return result

    def get_by_link(self, video_link):
        """ Return one video by its link """
        query = '''SELECT id from {TABLE_NAME} where video_link = "{video_link}" '''
        video = self.cur.execute(query)
        self.close() 
        return video.fetchone()

    def save_recomendation(self, video_info):
        ''' check if video already exists '''
        video_exists = self.get_by_link(video_info['video_id'])

        if video_exists:
            return True

        video_title = video_info['title'].replace('"', "'"),
        video_link = video_info['video_id'],
        thumbnail = video_info['thumbnail'],
        score = video_info['score']

        query = '''INSERT INTO {TABLE_NAME} (video_title, video_link, thumbnail, score) values 
                                ("{video_title}", "{video_link}", "{thumbnail}", {score});
                '''
        new_video = self.cur.execute(query)
        self.close()
    
    def like_video(self, liked_value, video_id):
        """" Edit liked column """
        update_time = datetime.datetime.now().strftime("%Y %m %d %H:%M:%S")


        query = '''update {TABLE_NAME} set liked = {liked_value},
                        updated_at = '{update_time}' where id = {video_id}
                '''
        self.cur.execute(query)
        self.close()

    def close(self):
        self.cur.close()
        self.conn.close()