FROM python:3.10-slim

RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /app


COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic && python manage.py runserver 0.0.0.0:8000"]
