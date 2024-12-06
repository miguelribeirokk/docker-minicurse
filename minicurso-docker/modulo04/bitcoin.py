import psycopg2
from flask import Flask
import requests

host = "my_postgres"
database = "meu_banco"
user = "meu_usuario"
password = "minha_senha"

app = Flask(__name__)
@app.route('/')
def home():
    try:
        conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        conn.close()
        data = requests.get('https://cointradermonitor.com/api/pbb/v1/ticker').json()
        return data
    except Exception as e:
        return "Erro com o banco de dados"

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)