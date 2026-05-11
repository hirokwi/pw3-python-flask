# pip install pymysql
# pip install flask-sqlalchemy

from flask_sqlalchemy import SQLAlchemy


# carregando sqlalchemy em uma variavel
db = SQLAlchemy()


# criando uma classe para representar a entidade Games no banco (tabela: games)

class Game(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)

    # metodo construtor

    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):

        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade


# criando uma classe para representar a entidade Consoles

class Console(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    fabricante = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)

    # metodo construtor

    def __init__(self, nome, fabricante, ano, preco, quantidade):

        self.nome = nome
        self.fabricante = fabricante
        self.ano = ano
        self.preco = preco
        self.quantidade = quantidade