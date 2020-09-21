# prima-italica
Test for a job https://www.pyjobs.com.br/job/1395/challenge_submit/

[![Build Status](https://travis-ci.org/codemodi/prima-italica.svg?branch=master)](https://travis-ci.org/codemodi/prima-italica)
[![codecov](https://codecov.io/gh/codemodi/prima-italica/branch/master/graph/badge.svg)](https://codecov.io/gh/codemodi/prima-italica)
### Instalação

#### Subir os containers 
 
 ```sh
$ docker-compose up --build
 ```

#### Rodar migrações
 ```sh
$ docker-compose run app python manage.py migrate
 ```
Acessar: http://localhost:8000/api/

| Recurso |      url      | Protocolo | Parametros |
|----------|:-------------|------:|----------:|
| Listar Voluntários |  /api/voluntario | GET | Nenhum |
| Incluir Voluntário |    /api/voluntario   | POST |  nome, sobrenome, bairro, cidade |
| Detalhes de um Voluntário | /api/voluntario/\<pk> | GET |  Id do voluntário |
| Alterar um Voluntário | /api/voluntario/\<pk> | PUT |  Id do voluntário, dados a atualizar |
| Remover um Voluntário | /api/voluntario/\<pk> | DELETE |  Id do voluntário |
| Listar Ações |  /api/acao | GET | Nenhum |
| Incluir Ação |    /api/acao   | POST |  nome_acao, instituicao_organizadora, endereco, bairro, cidade, descricao |
| Detalhes de uma Ação | /api/acao/\<pk> | GET |  Id da Ação |
| Alterar uma Ação | /api/acao/\<pk> | PUT |  Id da Ação, dados a atualizar|
| Remover uma Ação | /api/acao/\<pk> | DELETE |  Id da Ação |
