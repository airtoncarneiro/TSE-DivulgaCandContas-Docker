# TSE API (versão distribuída Kubernates)
Projeto para consumir as APIs do TSE visando o aprendizado de computação distribuída.
Tem-se por objetivo refatorar um antigo projeto monolítico para microserviços usando Kubernates, Spark e a núvem pública AWS.

### URL da API
https://divulgacandcontas.tse.jus.br/divulga/rest

### Dos endpoints
1. **/v1/eleicao/ordinarias/**<br>
Retorna todas as eleições ocorridas desde 2004.
(*aguardar novos endpoints)

### Da execução
O arquivo main.py é compartilhado por todos os microserviços, fazendo uma chamada específica ao serviço que será usado através da checagem da variável de ambiente **TSE_API**.
Atribuir:
* *eleicao_ordinaria* se o serviço a executar for para obter as eleições ordinárias.