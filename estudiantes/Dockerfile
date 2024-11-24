FROM python:3.9-slim

WORKDIR /app

# Establecer variables de entorno
ENV DB_NAME=estudiantes_db
ENV DB_USER=estudiantes_user
ENV DB_PASSWORD=estudiantes_password
ENV DB_HOST=10.128.0.82
ENV DB_PORT=5432

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
