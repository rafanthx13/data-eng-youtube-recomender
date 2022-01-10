# Registro do retorno de cada etapa

## Schema no Banco de Dados

````sql
CREATE TABLE IF NOT EXISTS public.data_engine_recomender
(
    id integer NOT NULL DEFAULT nextval('data_engine_recomender_id_seq'::regclass),
    video_title text COLLATE pg_catalog."default",
    video_link text COLLATE pg_catalog."default",
    thumbnail text COLLATE pg_catalog."default",
    score double precision,
    liked boolean DEFAULT false,
    created_at timestamp without time zone DEFAULT now(),
    updated_at date,
    upload_date text,
    CONSTRAINT data_engine_recomender_pkey PRIMARY KEY (id),
    CONSTRAINT data_engine_recomender_video_link_key UNIQUE (video_link)
)
````

## Chamados do `youtube_dl`

## Retorno de funções do projeto Flask

### `download_video_page`

Retorno do Download de uma página

````js
{
  'link': 'Q81zwSmaJo0',
  'uploader': 'DBA PRO',
  'title': 'O que é DATA WAREHOUSE? Você precisa de um?',
  'upload_date': '2017-09-26',
  'user': 'UC3Db4xY70lk3aZoUIgA2uKQ',
  'view_count': 57277,
  'like_count': 5619,
  'dislike_count': 0,
  'thumbnail': 'https://i.ytimg.com/vi_webp/Q81zwSmaJo0/maxresdefault.webp',
  'width': 1280,
  'height': 720,
  'categories': 'People & Blogs',
  'tags': 'o que é data warehouse|o que é armazem de dados|armazem de dados|data warehouse|data stage|o que é data stage|etl|o que é etl|extract transform and load',
  'channel_url': 'https://www.youtube.com/channel/UC3Db4xY70lk3aZoUIgA2uKQ',
  'description': 'Olá, tudo joia?................'
}
````

## Retorno da API

/show-video

````js
{
  "list_videos": [
    [
        
        53,
        "O que são Data Lakes?",
        "DqNdtR1dlgE",
        "https://i.ytimg.com/vi/DqNdtR1dlgE/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAyZrXwtL9-clq8K_eLJnvIFwSL3A",
        0.26153088378202527,
        false,
        "Mon, 10 Jan 2022 22:35:46 GMT",
        "2021-07-16"
            
    ],
  ],
    "status": "success",
}
````