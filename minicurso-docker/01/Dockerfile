FROM python:3.10-slim
WORKDIR /app
RUN pip install requests
COPY . .
CMD ["python", "for.py"]

# docker build -t modulo-01 .