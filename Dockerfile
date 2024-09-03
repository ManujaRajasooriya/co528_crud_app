FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir Flask

EXPOSE 5000

ENV FLASK_ENV=production

CMD ["python", "app.py"]
