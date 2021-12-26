# Copy Paste
import requests as rq
import bs4 as bs4
import re
import time
import youtube_dl 
import asyncio
import datetime
from requests_html import HTMLSession, AsyncHTMLSession

def download_search_page(keyword, n_of_videos):
    video_links = []
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    ydl = youtube_dl.YoutubeDL({"ignoreerrors": True, 'verbose':False, "date": today})
    # Faz a busca usando 
    result_search = ydl.extract_info("ytsearch{}:{}".format(n_of_videos, keyword),
                     download=False, extra_info={"date": today})
    # Altera cada elemnto do resultado
    for video_link in result_search['entries']:
         if video_link is not None:
            video_link['query'] = keyword
    video_links += result_search['entries']
    return video_links

def download_video_page(link):
    url = "https://www.youtube.com{link}"
    urll = url.format(link=link)
    response = rq.get(urll)
    link_name = re.search("v=(.*)", link).group(1)
    return response.text

def download_video_page(video_link):
    URL = "https://www.youtube.com/watch?v={link}"
    ydl = youtube_dl.YoutubeDL({"ignoreerrors": True, 'verbose':False})
    try:
        r = ydl.extract_info(url=URL.format(link=video_link), download=False)
        year = r['upload_date'][:4]
        month = r['upload_date'][4:6]
        day = r['upload_date'][6:]
    except Exception:
        return False
    
    video_info = {
        'link': video_link,
        'uploader': r['uploader'],
        'title': r['title'],
        'upload_date': f"{year}-{month}-{day}",
        'user': r['uploader_id'],
        'view_count': r['view_count'],
        'like_count': r['like_count'],
        'dislike_count': 0,
        'thumbnail': r['thumbnail'],
        'width': r['width'],
        'height': r['height'],
        'categories': '|'.join(r['categories']) if r['categories'] is not None else None,
        'tags': '|'.join(r['tags']) if r['tags'] is not None else None,
        'channel_url': r['channel_url'],
        'description': r['description']
    }

    return video_info