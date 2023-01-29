FROM python:2.7-slim

WORKDIR app/
COPY /requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV IS_DOCKER=True

CMD ./manage.py runserver 0.0.0.0:8000