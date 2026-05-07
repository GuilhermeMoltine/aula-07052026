## Sistema de Gestão de Rede de Cinemas 
## Descrição do Projeto
Este projeto tem como objetivo desenvolver um sistema para gerenciamento de uma rede de cinemas, permitindo o controle de cinemas, filmes, sessões e público das exibições.
O sistema possibilita cadastrar cinemas e filmes, organizar sessões e consultar informações relacionadas aos filmes em cartaz e quantidade de espectadores.
 Levantamento de Requisitos
✅ Requisitos Funcionais (RF)
RF01 – Cadastrar Cinema
O sistema deve permitir cadastrar cinemas com os seguintes dados:


Nome


Cidade


Estado


Endereço


Capacidade de público



RF02 – Cadastrar Filme
O sistema deve permitir cadastrar filmes contendo:


Título


Duração


Gênero


Diretor


Elenco



RF03 – Cadastrar Sessão
O sistema deve permitir cadastrar sessões informando:


Filme


Cinema


Horário


Sala


Data



RF04 – Registrar Público
O sistema deve permitir registrar a quantidade de espectadores de cada sessão.

RF05 – Consultar Filmes em Cartaz
O sistema deve permitir visualizar os filmes exibidos em cada cinema.

RF06 – Consultar Público
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



🏗️ Diagrama de Classes do Domínio
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



🔗 Relacionamentos


Um Cinema pode possuir várias Sessões.


Um Filme pode estar presente em várias Sessões.


Cada Sessão pertence a um único Cinema.


Cada Sessão exibe apenas um Filme.









