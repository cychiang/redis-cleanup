FROM python:3.6-alpine3.8

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt

WORKDIR /app
COPY app.py /app

CMD python3 app.py