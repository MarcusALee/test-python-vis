FROM python:3.7

#RUN apt-get update && apt-get install -y procps

COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

COPY python_vis_1_dashapp.py /app
WORKDIR /app

CMD gunicorn -b 0.0.0.0:80 app:server
