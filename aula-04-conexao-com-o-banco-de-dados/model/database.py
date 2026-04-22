# pip install pymsql
# pip install flask-sqlalchemy

from flask_sqlalchemy import SQLAlchemy


# carregando sqlalchemy em uma variavel
db = SQLAlchemy()

# criando uma classe para representar a entidade Games no banco (tabela: games)

class Game(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.Integer)
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.String(150))
    quantidade = db.Column(db.Float)
    
    #  metodo construtor
    
    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade