from alpine:latest

RUN apk add py3-pip
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt                                                                            

ENV FLASK_APP=src
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

ENTRYPOINT ["flask", "run"]
