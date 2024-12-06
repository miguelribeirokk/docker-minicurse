FROM python:3.10-slim
WORKDIR /app
RUN pip install flask
RUN pip install psycopg2-binary
RUN pip install requests
COPY . .
CMD ["python", "app.py"]

