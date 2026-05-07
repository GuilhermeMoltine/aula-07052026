## Sistema de Gestão de Rede de Cinemas 
## Descrição do Projeto
Este projeto tem como objetivo desenvolver um sistema para gerenciamento de uma rede de cinemas, permitindo o controle de cinemas, filmes, sessões e público das exibições.
O sistema possibilita cadastrar cinemas e filmes, organizar sessões e consultar informações relacionadas aos filmes em cartaz e quantidade de espectadores.
 Levantamento de Requisitos
Requisitos Funcionais (RF)
## RF01 – Cadastrar Cinema
O sistema deve permitir cadastrar cinemas com os seguintes dados:


Nome


Cidade


Estado


Endereço


Capacidade de público



## RF02 – Cadastrar Filme
O sistema deve permitir cadastrar filmes contendo:


Título


Duração


Gênero


Diretor


Elenco



## RF03 – Cadastrar Sessão
O sistema deve permitir cadastrar sessões informando:


Filme


Cinema


Horário


Sala


Data



## RF04 – Registrar Público
O sistema deve permitir registrar a quantidade de espectadores de cada sessão.

## RF05 – Consultar Filmes em Cartaz
O sistema deve permitir visualizar os filmes exibidos em cada cinema.

## RF06 – Consultar Público
O sistema deve permitir consultar:


Público por sessão


Público por filme


Público por cinema



## Regras de Negócio (RN)
RN01
Uma sessão deve estar vinculada a apenas um filme.
RN02
Um cinema pode possuir várias sessões simultaneamente.
RN03
A quantidade de espectadores não pode ultrapassar a capacidade do cinema.
RN04
Deve existir intervalo mínimo entre sessões.
RN05
Um filme pode estar em cartaz em vários cinemas.
RN06
Toda sessão deve possuir data e horário definidos.

 
## Diagrama de Casos de Uso (Visão Geral)
Atores
Funcionário / Administrador
Responsável pelo gerenciamento do sistema.
Espectador
Usuário responsável por consultar informações das sessões e filmes.

Casos de Uso
Funcionário / Administrador


Cadastrar Cinema


Cadastrar Filme


Cadastrar Sessão


Registrar Público


Consultar Relatórios


Espectador


Consultar Filmes em Cartaz


Consultar Sessões



## Diagrama de Classes do Domínio
Classe: Cinema
Atributos


idCinema


nome


cidade


estado


endereco


capacidade



Classe: Filme
Atributos


idFilme


titulo


duracao


genero


diretor


elenco



Classe: Sessao
Atributos


idSessao


data


horario


sala


publico



## Relacionamentos


Um Cinema pode possuir várias Sessões.


Um Filme pode estar presente em várias Sessões.


Cada Sessão pertence a um único Cinema.


Cada Sessão exibe apenas um Filme.



## Diagrama de Casos de Uso

<img width="474" height="546" alt="image" src="https://github.com/user-attachments/assets/fbf228a3-d445-470b-b759-8bddb1e5c79f" />


## Diagrama de Classes 

<img width="200" height="364" alt="image" src="https://github.com/user-attachments/assets/dced8303-aa90-4183-a41f-6feebcc20705" />

## Diagrama de Atividade — Cadastrar Filme

<img width="190" height="333" alt="image" src="https://github.com/user-attachments/assets/9a37d459-a3c3-4a10-9a3a-bf45a7494b46" />

## Diagrama de Atividade — Registrar Público

<img width="351" height="452" alt="image" src="https://github.com/user-attachments/assets/a2d8d109-298b-4b75-a881-c5340e10576c" />

## Diagrama de Sequência — Cadastrar Filme

<img width="718" height="457" alt="image" src="https://github.com/user-attachments/assets/94277cdd-64a5-47fc-9c3c-0ecd5ed1f524" />

## Diagrama de Sequência — Registrar Público

<img width="756" height="501" alt="image" src="https://github.com/user-attachments/assets/ea587503-9143-4829-b564-bcacf01b77cf" />







