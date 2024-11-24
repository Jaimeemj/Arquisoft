FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
# Ejemplo de ejecución del contenedor:
# docker run -d -e POSTGRES_DB=mydb -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypass -e MONGO_URI=mongodb://user:pass@host:port -p 8080:8080 <image_name>
