FROM python:3.8

COPY . /app

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
