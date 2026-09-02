# importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# criando uma instância do SQLAlhemy
# carregando o SQLAlchemy em uma variável
db = SQLAlchemy()

# criando a classe para representar a entidade Games no banco de dados (tabela: sempre no singular e começa com letra Maiúscula)
class Game(db.Model):
    #colunas da tabela
    #chave primaria 
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
    # Metodo construtor -> atributos que serão utilizados pelos objetos
    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade
        
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
        
    #tabela de usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha