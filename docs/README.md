## Documentação do projeto



## Links úteis

Link do curso: https://curso.mariofilho.com/

Web App do Curso de Mário: https://sheltered-reef-65520.herokuapp.com/

+ Esse projeto é estático, não é atualizado

Palestra das 5 etapas: https://youtu.be/KL8qBKAHn_A



## Usando `virtualenv`

Instalar lib

````sh
pip install virtualenv
````

Criar env

````sh
virtualenv venv_name
````

Ativar ambiente (deve aparecer env no terminal)

````sh
# linux/mac
source venv/bin/activate (Linux ou macOS)
# windows
venv/Scripts/Activate (Windows)
````

Desativar ambiente

````sh
deactivate
````

requirements.txt

````sh
# salvar libs do ambiente
pip freeze > requirements.txt
# instalar de acordo com as libs do arquivo
pip install -r requirements.txt
````



## Principais Features e Aprendizado do projeto

+ Scrap Youtube com `youtube-dl`

+ Active Learning para Label dataset a partir de uma base feita manualmente

+ Bayesian Optimization (para LightGBM) e Ensemble Models



## Rodar Flask


````sh
# bash/sh linux
$ export FLASK_APP=hello
````


````sh
# CMD
$ set FLASK_APP=hello
````


````sh
# PowerShell
> $env:FLASK_APP = "hello"
````


**IMPORTANTE SOBRE O FLASK**

Não rodar `flask run` porque ele não consegue ler submodules nem as pastas direito, execute com 
``python app.py``



## Git Branch

**Criar nova branch e vai para ela**

````sh
git checkout -b new_branch
````

Isso é um atalho para

````sh
$ git branch new_branch
$ git checkout new_branch
````

**Trocar de Branch**

````sh
git checkout MinhaNovaBrach
````

**Publicar nova branch**

````sh
git push --set-upstream origin MinhaNovaBrach
````

**Merge Branchs**

Você tem que ir para a branch do heroku, e lá faz o merge com main, aí agora o heroku vai estar atualizado como a main

````sh
git checkout heroku
git merge main
git push
````



## Mario Filho - Iniciar projeto de Data Science



### Passar da ideia para um projeto de DS

Pegue um problema que seja realmente desafiador. Vamos pegar o seguinte problema.

- Mario Filho sempre fica procurando vídeos desses assuntos no Youtube. Acontece que são enviados 500h por minuto para o youtube, e não é qualquer vídeo de DS que ele quer, ele quer coisa avançadas


**Esquematizando o projeto**

Qual é o Problema?

+ Gasto muito tempo buscando novos vídeos no Youtube

Qual a solução ideal?

+ Ter uma lista apenas dos vídeos que eu, com certeza, vou gostar.

Como eu posso fazer isso com Data Science/ML?
Criar uma solução de recomendação de vídeos

Como essa solução será usada em produção?

+ Abordagem com "ponto de corte" -> Ex: retornar apenas Top 3
+ Abordagem de ranking -> ordene os vídeos mais interessantes primeiro
+ Web app com os vídeos (links) e as previsões ordenadas

Como eu vou saber que deu certo?

+ Métrica primária: dos top N vídeos, quantos eu coloco na lista de Watch Later e vejo mesmo
+ Métrica(s) secundária(s): quanto tempo eu passo selecionando vídeos

**Qual é a primeira solução para Mario filhos para escolher um vídeo**

Ele escolhe:

+ Vídeo com mais de 20 min
+ geralmente bem mais técnico (de seminário)



###  Portfólio de Data Science

**Ideias para iniciar**

+ Selecione um problema simples que já foi resolvido, mas que faça para você mesmo

**Sugestões de Projetos pro seu Portfólio**

Como escolher o problema para trabalhar?

+ Escolha Problema simples de algo já resolvido

**O que as empresa mais gostam de ver são**

+ Recomendação (aumento de vendas, marketing)
+ Time Series (previsão de demanda, cancelamento) 
  - Nosso caso será em timeSeries

**Em que área escolher**

+ Escolha algo que seja do seu interesse, ou que, pelo menos, resolva algum problema real seu.

**Onde buscar os dados**

+ Kaggle, Google Dataset Search

**Fontes de informação**

+ Faça uma lista de "fontes de informação" ideais para resolver o seu problema

**Qual o mínimo de dados que eu preciso?**

+ Para nosso trabalho é: Características dos videos (título) e uma label, anotação
+ Vou buscar os vídeos fazendo 'search' com as seguintes queries no mecanismo de busca do youtube. queries = [machine learning, kaggle, data science]

