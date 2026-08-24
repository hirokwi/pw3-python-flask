# comentário em Python
# importando o Flask na aplicação
from flask import Flask, render_template 
# render_template renderiza as páginas html
from controllers import routes
#importando o pymysql
import pymysql
# importando o model de games
from models.database import db, Game

# carregando o Flask em uma variável
# declarando variável no python
app = Flask(__name__, template_folder='views')

#__name__ é uma variável de ambiente do Python que tem o nome do módulo atual

#definindo o nome do banco de dados
DB_NAME = 'thegames'

# passando o nome do banco para o flask
app.config['DATABASE_NAME'] = DB_NAME

# passando o endereço do banco para o flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

# criando uma chave secreta (para flash messages e sessões)
app.config['SECRET_KEY'] = 'meusegredo'

# definindo o tempo da sessão
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 # 1 hora

#Eviando a variável APP (FLASK) para as rotas
routes.init_app(app)

# iniciando o servidor web (tipo apache, mas no python faz aqui mesmo)
if __name__ == '__main__':
    # passando os dados e criando a conexao com o banco
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    # tentando a conexao com o banco
    try:
        with connection.cursor() as cursor:
            # cria o banco se ele nao existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print("O banco de dados foi criado com sucesso!")
    except Exception as error:
        print(f"Erro ao criar o banco de dados: {error}")
        #fechando a conexao
    finally:
        connection.close()
    
    # inicializar o SQLAlchemy
    db.init_app(app=app)
    with app.test_request_context():
        #criando as tabelas
        db.create_all()
        #inicia o servidor
    app.run(debug=True)
    # verificando se app for o arquivo principal, ele inicia o servidor
    # debug=True ligando modo de depuração, reinicia automático, só não funciona quando tem erro no código, aí tem que rodar manualmente
    
# main é quando se está testando se é arquivo principal, se for, dá run, que inicia o servidor.