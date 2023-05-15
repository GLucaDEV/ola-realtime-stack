FROM python:3.9.13-alpine3.16

RUN mkdir /code

WORKDIR /code

RUN mkdir /code/logs

COPY . /code

ENV FLASK_APP=endpoint.py
ENV FLASK_RUN_HOST=0.0.0.0


RUN apk add --no-cache gcc musl-dev linux-headers


RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["flask", "run"]
