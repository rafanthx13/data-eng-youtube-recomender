# Data Engineering Youtube Videos Recommender

Baseado no curso de Mário filho e no Repo [cesarvinici](https://github.com/cesarvinici/recomendador-videos-youtube)



Projeto de Data Science para criação de recomendador de vídeos do youtube para a temática de Engenharia de Dados.

Foi construído uma API Flask com deploy no heroku com as seguintes funções:
+ `/show-videos` Retornar os 20 vídeos mais bem avaliados pelo modelo
+ `/update-db` Busca novos vídeos para ser adicionados no DB após avaliados pelo modelo


Para deploy, use a branch `heroku`




## Como executar projeto

1. Arquivos de Jupyter Notebook
   + 1- Cria Dataset via Web Scrap pela lib `youtube_dl` dos links das pesquisas do youtube para os seguintes termos `data-engineering, data pipeline e airflow'
   + 2- Para cada vídeo da etapa anterior mais detalhes internos sobre os mesmos
   + 3- Em seguida há duas opções para a 'label' desses vídeos:
     + 1- Preencher o dataset manualmente até a metade e usar Active Learning para preencher o resto (notebooks de número 03)
     + 2- Preencher tudo manulamentes (demora cerca de 1h, mas assim vai direto para o notebook 04)
   + 4- Com os vídeos já classificados no dataset podemos então criar modelos de ML para prever. Por fim há a opção de usar ensemble models (colocar porcentagem sobre os modelos e assim obter alguma otimização)
2. Criação de API
   + 1- Projeto em flask com a lib `virtualenv` usando `requirements.txt` para importar as libs em python
   + 2- Lib `psycopg2` para acessar banco de dados postgre do heroku que tem 1Gb de espaço


OBS: Arquivo `dataset-completo-labeled.csv` tem o dataset com as labels

