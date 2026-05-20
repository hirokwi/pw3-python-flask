# Importando o Flask na aplicação
from flask import Flask, render_template
from controllers import routes

import pymysql
from model.database import db, Game

# Declarando variável do banco
DB_NAME = "thegames"

# Carregando o Flask
app = Flask(__name__, template_folder='views')

# Configurações do banco
app.config['DATABASE_NAME'] = DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

# Inicializando rotas
routes.init_app(app)

if __name__ == '__main__':
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print("Banco criado com sucesso")
    except Exception as error:
        print(f"Erro ao criar banco: {error}")
    finally:
        connection.close()
        # Inicializar o SQLAlchemy
        db.init_app(app=app)
        with app.test_request_context():
            db.create_all()

    # Iniciando servidor
if __name__ == '__main__':
    app.run(debug=True)
    
