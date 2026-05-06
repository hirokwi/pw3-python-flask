from flask import render_template, request, redirect, url_for
from model.game import listar_games, adicionar_game
# importando o model game e o sqlalchemy
from model.database import Game


def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        return render_template(
            'games.html',
            game={
                "titulo": "Warframe",
                "ano": 1999,
                "categoria": "RPG"
            },
            jogadores=['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antonio']
        )

    @app.route('/consoles')
    def consoles():
        return render_template(
            'consoles.html',
            nome="Nintendo Switch",
            lançamento=1969,
            marca="Nintendo",
            consoles=['PS4', 'Xbox', 'Nintendo Switch', 'PS5', 'PS1']
        )

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():

        if request.method == 'POST':

            titulo = request.form.get('titulo')
            ano = request.form.get('ano')
            categoria = request.form.get('categoria')

            if titulo and ano and categoria:
                adicionar_game(titulo, ano, categoria)

            return redirect(url_for('cadgames'))

        return render_template('cadgames.html', listaGames=listar_games())
    
    @app.route("/estoque_jogos")
    def estoque_jogos():
        games = Game.query.all()
        return render_template('estoque_jogos.html', games=games)