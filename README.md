# Truco

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Número do Grupo**: 04<br>
**Paradigma**: Sistemas Multiagentes<br>

## Alunos
| Foto | Matrícula | Nome | GitHub |
|:--:|:--:|:--:|:--:|
| <img src="./images/members/andre.jpg" width="100">| 15/0005563 | Andre Lucas Ferreira Lemos de Souza | [@andrelucasf](https://github.com/andrelucasf) 
| <img src="./images/members/ruan.jpg" width="100">| 18/0030272 | Antonio Ruan Moura Barreto | [@RuanMoura](https://github.com/RuanMoura) 
| <img src="./images/members/brenda.jpg" width="100">| 18/0041444 | Brenda Vitória dos Santos | [@brendavsantos](https://github.com/brendavsantos)
| <img src="./images/members/estevao.jpg" width="100">| 18/0052616 | Estevão de Jesus Reis | [@estevaoreis25](https://github.com/estevaoreis25)
| <img src="./images/members/joao.jpg" width="100">| 18/0033743 | Joao Pedro Silva de Carvalho | [@jps12](https://github.com/jps12) 
| <img src="./images/members/sergio.jpg" width="100">| 18/0037439 | Sérgio de Almeida Cipriano Junior | [@sergiosacj](https://github.com/sergiosacj) 
| <img src="./images/members/thiago.jpg" width="100">| 18/0028324 | Thiago Luiz de Souza Gomes| [@thiagomesUNB](https://github.com/thiagomesUNB) 
| <img src="./images/members/victor.jpg" width="100">| 18/0028685 | Victor Samuel dos Santos Lucas| [@victordsantoss](https://github.com/victordsantoss) 
| <img src="./images/members/vini.jpg" width="100">| 17/0115500 | Vinicius Vieira de Souza | [@faco400](https://github.com/faco400) 

## Sobre 
O projeto do paradigma de sistemas multiagentes visa desenvolver uma aplicação do jogo truco (com todas as regras do tipo paulista) utilizando python.

## Screenshots
Adicione 2 ou mais screenshots do projeto em termos de interface e/ou funcionamento.

## Instalação 
**Tecnologias**:   
Para utilizar o pip nas instalações necessárias para o projeto, é necessário obter o python. Para isso:  
1. Atualize alista de pacotes e instale os pré-requisitos:
```
$ sudo apt update
$ sudo apt install software-properties-common
```
2. Adicione os _deadsnakes_ a sua lista:
```
$ sudo add-apt-repository ppa:deadsnakes/ppa
```
3. Finalmente, instale o python (depreferência a ultima versão, mas utilizamos a 3.9 no exemplo)
```
$ sudo apt install python3.9
```
4. E utilize o próprio python para obter o pip
```
$ python get-pip.py
```
- jupyter (Python interactive notebook)  
```
$ pip install notebook
```
- matplotlib (Python’s visualization library), source install from git
```
$ git clone git://github.com/matplotlib/matplotlib.git
```
```
$ cd matplotlib 
``` 
```
$ python setup.py install
```
- mesa (ABM library)
```
$ pip install mesa
```
- numpy (Python’s numerical python library)
```
$ pip install numpy   
```

## Sobre o Jogo

É o tipo de truco mais comum nas jogatinas, tanto online, como em competições. É utilizado um baralho com 40 cartas (exclui-se os 8, 9, 10 e os coringas) com duas duplas.

A distribuição das cartas é feita aleatoriamente, não havendo a intervenção de nenhum jogador ou membro da equipe, sendo distribuídas 3 cartas por participante.

O objetivo é marcar 12 pontos primeiro através da mão batida (uma combinação de cartas que gera no mínimo um ponto por rodada, que pode ser aumentada até 12 dependendo da aposta e das opções de cartas entre as duplas).


Cada mão é definida em três rodadas. Em cada rodada, os jogadores recebem 3 cartas, que devem ser colocadas à mesa e trocadas uns com os outros e no montante de cartas devidamente embaralhado.

No final da rodada, a combinação com maior pontuação ganha a mão.

Lembrando que Manilha é a carta mais forte da partida, depois do 3, e dos naipes, sendo a carta inicial na qual o primeiro jogador vira para cima antes do jogo começar, chamada de “Vira”. Toda combinação que levar esta carta terá uma pontuação maior no somatório final da rodada.

## Uso 
Explique como usar seu projeto, caso haja algum passo a passo após o comando de execução.

## Vídeo
Adicione 1 ou mais vídeos com a execução do projeto.

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas a seguir.

## Fontes
Caso utilize materiais de terceiros, referencie-os adequadamente.
