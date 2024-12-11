# Use the official Python image from the Docker Hub
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN rm /app/requirements.txt

COPY . .

ENV FLASK_APP=app
ENV FLASK_ENV=debug

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]
