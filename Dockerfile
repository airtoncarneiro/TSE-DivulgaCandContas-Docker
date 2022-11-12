FROM python:3.10.8-alpine
WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .
ARG ENV=ordinarias
ENV TSE_API=${ENV}

CMD ["python", "main.py"]

# docker build -t tse/candidatos .
# docker run --name tse-ordinarias -it --rm --entrypoint sh tse/candidatos
# docker volume create tse-datas