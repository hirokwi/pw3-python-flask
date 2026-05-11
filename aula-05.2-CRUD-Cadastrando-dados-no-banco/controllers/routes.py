from flask import render_template, request, redirect, url_for
from model.game import listar_games, adicionar_game
from model.database import Game, Console, db


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

        return render_template(
            'cadgames.html',
            listaGames=listar_games()
        )

    @app.route('/estoque_jogos', methods=['GET', 'POST'])
    def estoque_jogos():

        if request.method == 'POST':

            dados_form = request.form.to_dict()

            newGame = Game(
                titulo=dados_form['titulo'],
                ano=dados_form['ano'],
                categoria=dados_form['categoria'],
                plataforma=dados_form['plataforma'],
                preco=dados_form['preco'],
                quantidade=dados_form['quantidade']
            )

            db.session.add(newGame)
            db.session.commit()

            return redirect(url_for('estoque_jogos'))

        games = Game.query.all()

        return render_template(
            'estoque_jogos.html',
            games=games
        )

    @app.route('/estoque_jogos/delete/<int:id>')
    def deletar_jogo(id):

        game = Game.query.get(id)

        if game:
            db.session.delete(game)
            db.session.commit()

        return redirect(url_for('estoque_jogos'))

    @app.route('/estoque_consoles', methods=['GET', 'POST'])
    def estoque_consoles():

        if request.method == 'POST':

            dados_form = request.form.to_dict()

            newConsole = Console(
                nome=dados_form['nome'],
                fabricante=dados_form['fabricante'],
                ano=dados_form['ano'],
                preco=dados_form['preco'],
                quantidade=dados_form['quantidade']
            )

            db.session.add(newConsole)
            db.session.commit()

            return redirect(url_for('estoque_consoles'))

        consoles = Console.query.all()

        return render_template(
            'estoque_consoles.html',
            consoles=consoles
        )

    @app.route('/estoque_consoles/delete/<int:id>')
    def deletar_console(id):

        console = Console.query.get(id)

        if console:
            db.session.delete(console)
            db.session.commit()

        return redirect(url_for('estoque_consoles'))