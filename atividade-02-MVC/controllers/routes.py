from flask import render_template, request, redirect
from models.music import listar_musicas, adicionar_musica

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/form')
    def form():
        return render_template('form.html')

    @app.route('/cadastrar', methods=['POST'])
    def cadastrar():
        nome = request.form.get('nome')
        artista = request.form.get('artista')
        genero = request.form.get('genero')
        duracao = request.form.get('duracao')

        adicionar_musica(nome, artista, genero, duracao)

        return redirect('/list')

    @app.route('/list')
    def lista():
        musicas = listar_musicas()
        return render_template('list.html', musicas=musicas)