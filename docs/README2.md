# Passo a Passo
1. Criar o modelo [x]
2. Testar app localmente em flask
  - virtual env
    - virtualenv nome_da_virtualenv ;;
    source env/bin/activate (Linux ou macOS)
     env/Scripts/Activate (Windows) {deve aparecer env}
deactivate
  - ao executar 'pip list' aparece so 3 pacotes
    - pip freeze > requirements.txt
     - pip install -r requirements.txt
  - 
  - 

3. rodar flask

onde hello [e  nome do arquiv inicial de python que importa falsk
bash/sh linux
$ export FLASK_APP=hello
$ flask run
 * Running on http://127.0.0.1:5000/

CMD

> set FLASK_APP=hello
> flask run
 * Running on http://127.0.0.1:5000/

Power-sheçç

> $env:FLASK_APP = "hello"
> flask run
 * Running on http://127.0.0.1:5000/

## COMO RODAR

usa-se virtual env

 env/Scripts/Activate

depois isntalla dependencias do pip

> $env:FLASK_APP = "app"
> flask run

# Return Type

{
  "list_videos": [
    [
      14, 
      "Airflow for Beginners - Run Spotify ETL Job in 15 minutes!", 
      "i25ttd32-eo", 
      "https://i.ytimg.com/vi/i25ttd32-eo/maxresdefault.jpg", 
      0.6828606848631272, 
      false
    ], 
    [
      3, 
      "What is Data Pipeline | How to design Data Pipeline ? - ETL vs Data pipeline", 
      "VtzvF17ysbc", 
      "https://i.ytimg.com/vi/VtzvF17ysbc/maxresdefault.jpg", 
      0.6812849375659183, 
      false
    ], 
  ], 
  "status": "success"
}