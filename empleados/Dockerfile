FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
# Para ejecutar el contenedor con las credenciales:
# docker run -d -e POSTGRES_DB=mydb -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypass -e POSTGRES_HOST=myhost -p 8080:8080 <image_name>
