Criar nova branch e vai para ela
git checkout -b MinhaNovaBrach
Isso é um atlaho paara
$ git branch iss53
$ git checkout iss53

Trocar de Branch
git checkout MinhaNovaBrach

Publicar nova branch
git push --set-upstream origin MinhaNovaBrach

## Merge

Voce tem que ir para a bracnh do heroku, e la faz com main, ai agora o heroku vai estar atualizado como a main

git checkout heroku
git merge main
git push