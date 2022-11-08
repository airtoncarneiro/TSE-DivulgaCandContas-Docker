FROM python:3.10.8-alpine
WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

ENV TSE_API ordinarias

CMD ["python", "main.py"]


# docker run --name tse-cand -it --rm --entrypoint sh img_tsecand
# docker volume create tse-datas