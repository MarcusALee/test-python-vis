FROM python:3.7

COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

COPY python_vis_1_dashapp.py /app/
COPY test.csv /app/
WORKDIR /app
#COPY python_vis_1_dashapp.py /

CMD gunicorn -b 0.0.0.0:80 app:server
