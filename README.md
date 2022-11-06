# TSE API (versão distribuída Kubernates)
Projeto para consumir as APIs do TSE visando o aprendizado de computação distribuída.
Tem-se por objetivo refatorar um antigo projeto monolítico para microserviços usando Kubernates, Spark e a núvem pública AWS.

### URL da API
https://divulgacandcontas.tse.jus.br/divulga/rest

### Dos endpoints
1. **/v1/eleicao/ordinarias/**<br>
Retorna todas as eleições ocorridas desde 2004.  

2. **/v1/eleicao/buscar/{uf}/{id}/municipios
> Onde:  
>> {uf}: Sigla da unidade federativa  
>> {id}: Código que cada eleição recebe  

3. **/v1/candidatura/listar/{ano}/{codigo}/{id}/{tipo}/candidatos
> Onde:  
>> {ano}: Ano da eleicao  
>> {codigo}: Código do município  
>> {id}: Código que cada eleição recebe  
>> {tipo}: 11, 12 ou 13, prefeito, vice-prefeito ou vereador, respectivamente  

4. **/v1/candidatura/buscar/{ano}/{codigo}/{id}/candidato/{codCand}
> Onde:  
>> {ano}: Ano da eleicao  
>> {codigo}: Código do município  
>> {id}: Código que cada eleição recebe  
>> {codCand}: Código do candidato   

### Da execução
O arquivo main.py é compartilhado por todos os microserviços fazendo uma chamada específica ao serviço que será usado através da checagem da variável de ambiente **TSE_API**.
Atribuir:
* *ordinaria* se o serviço a executar for para obter as eleições ordinárias.  
* *municipios* se for para obter a lista de municípios de uma eleição.
* *candidatos* se para para obter a lista de candidatos de uma eleição e município.