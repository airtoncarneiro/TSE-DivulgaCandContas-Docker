FROM python:3.10.8-alpine
WORKDIR /app

COPY . .
COPY ./requirements.txt .

#RUN apk add tzdata
#RUN --rm -it -e TZ=America/Sao_Paulo debian date

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

#ARG ENV=ordinarias
#ENV TSE_API=${ENV}
#ENV TZ=America/Sao_Paulo

#CMD ["python", "main.py"]

# docker build -t tse_cand_contas:v0.4 .
# docker run --name tse-ordinarias -it --rm --entrypoint sh tse/candidatos
# docker volume create tse-datas


#  docker-compose rm --all &&
#  docker-compose pull &&
#  docker-compose build --no-cache &&
#  docker-compose up -d --force-recreate

# docker system df --format 'table {{.Type}}\t{{.TotalCount}}\t{{.Size}}'
# docker build prune
# docker system df prune -a

# docker run -t -d -P -v "D:\Proj\TSE - Candidaturas\Kubernates\desafio-airton":/app --name teste tse_cand_contas:latest