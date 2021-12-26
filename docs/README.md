# OU EU FAÇO ISSO TUDO DO ZERO OU SÓ VOU PERDER TEMPO. ESTOU COM SONO E CADA VEZ QUE MECHO NISSO TNEHO UM NOVO PROBLEMA, É UMA MALDIÇÃO

Próximos passos executar passo a passo, gera todos os modelos no develop

# DS Project - Youtube Recomendation System

======================== INCOMPLETO ======================== 

## Status do Projeto

Criado: 11/12/2021 || Last Update: 12/12/2021

**Status**

+ Nâo consegui nem executar docker de cesar

**OBS**
+ Não há mais número de dislikes

**OBS mario-filho-original**
+ nao usei random-forets pois precisa fazer um rebuild
  - Dá o erro de ModuleNotFoundError: No module named 'sklearn.ensemble.forest'


## Links úteis

Link do curso: https://curso.mariofilho.com/

Web App do Curso: https://sheltered-reef-65520.herokuapp.com/

Palestra das 5 etapas: https://youtu.be/KL8qBKAHn_A

Kaggle Datasets: https://www.kaggle.com/datasets​

Google Dataset Search: https://datasetsearch.research.google.com/



## Principais Features e Aprendizado do projeto

+ Scrap Youtube com `yoytube-dl`

+ Active Learnig para Label dataset apartir de uma base feia manualmente

+ Baysian Optmization (para LightGBM) e Ensemble Models

## Objetivo das Aulas

### Módulo 1

#### Passar da ideia para DS

Pegue um problema que seja realmente desafiador. Vamos pegar o seuginte problema.

- Mario Filho sempre fica procurando vídeos disos no Youtube. Acontece que sâo enviados 500h por minuto para o youbue, e não é qualquer vído de DS que ele quer, ele quer coisa avanaçadas


**Esquematizando o projeto**

Qual é o Problema?

+ Gasto muito tempo buscando novos vídeos no Youtube

Qual a solução ideal?

+ Ter uma lista apenas dos vídeos que eu, com certeza, vou gostar.

Como eu que posso fazer isso com Data Science/ML?
Criar uma solução de recomendação de vídeos

Como essa solução será usada em produção?

+ Abordagem com "ponto de corte" -> Ex: retornar apenas Top 3
+ Abordagem de ranking -> ordene os vídeos mais interessantes primeiro
+ Web app com os vídeos (links) e as previsões ordenadas

Como eu vou saber que deu certo?

+ Métrica primária: dos top N vídeos, quantos eu coloco na lista de Watch Later e vejo mesmo
+ Métrica(s) secundária(s): quanto tempo eu passo selecionando vídeos

**Qual é a primeira soluçâo para Mario filhos apra escolher um vídeo**

Ele escolhe:

+ Vídeo com mais de 20min
+ geralmente bem mais técnico (de seminário)

####  Portifolio de DataScience

**Ideias para iniciar**

+ Selecione um problema simples que já foi resolvido, mas que faça para você mesmo

**Sugestoos de Projetos pro seu Portifolio**

Como escolher o problema pra trabalhar?

+ Escolha Problema simples de algo já resolvido

**O que as empresa mais gostam de ver são**

+ Recomendação (aumento de vendas, marketing)
+ Time Series (previsão de demanda, cancelamento) 
  - Nosso caso será em timeSeries

**Em que área escolher**

+ Escolha algo que seja do seu interrese, ou que, pelo menos, resolva algum problema real seu.

**Onde buscar os dados**

+ Kaggle, Google Dataset Search

**Fontes de informaçâo**

+ Faça uma lista de "fontes de informação" ideais para resolver o seu problema

**Qual o mínimo de dados que eu preciso?**

+ Para nosso trabalho é: Características dos vídeos (título) e uma label, anotação
+ Vou busca os vídeos fazenod 'search' com as seguintes queries no mecanismo de busca do youtube. queries = [machine learning, kaggle, data science]

## 

### Módulo 4

+ 41- app.py
+ 42 - run_backend
+ 43 - get_data.py e ml_utils.py
+ 44 - Dockerfile e somente esse arquivo
+ 45 - db_stater
  + deixamos para atualziar a base mais seperada, pois esse processo é demoradao e nao quermeos que interrompa o user
+ 46 - Comandos para subir Container DOcker da APP FALSK. Mostra a seeri de comandos par asubri no heroku
+ 47 -analisando os videos se estão mesmo interresantes
  + Dicas de como incrmemtenra : Ex: analisar os canais de que vocÊ gosta de da rum booetser neses canais

### Módulo 5

#### Salvar em uma tabela SQL com SQLite

+ Adaptar os script para funcionar com um banco de dados SQL (SQL-Lite)
+ Criar endpoint de api
+ colocou '#' nas linhas novas

usamos 'wtiht' na parte de 'sql.connect' pois qasisnm nao rpecisa dizer explicitamente para fechar a conexao, ela vai ta ativa,e xeceutar e fechar por causa do 'with'

**O BANC DE DADOS É CRIADO QUANDO É ESCRITO O DOCKER**

db_stater = Criamos agora um CREATE TABLE para o SQLITE, antes do APP subir, esse arquivo cria a tabela no arquivo do SQLite.

run_bacnkend = tambem é alterado

get_data = também é alterado. Colocamos header para voltar páginas do youtube de origem em pt-br

ml_utils = nao mudou nada

**Infeim, agora, ao vinzes de arameznar os dados em JOSN slava em arquivo SQLITE**

#### Criar API de predict

Criamos uma segunda rota `/predict`.

`request.args.get`: vaibuscar os argumetnos da requsiçâo get, ou seja **DADOS DA URL** no flask.

Se estiver a URL lá, vai buscar dados daquele vídeo, usar o mdoelo e retorna.

Será uma API para fazer uma previsâo apra um caso novo

