from flask import render_template, request, redirect, url_for, flash
from model.game import listar_games, adicionar_game
from markupsafe import Markup
from model.database import Game, Console, db, Usuario
from werkzeug.security import generate_password_hash


def init_app(app):

    # Página inicial
    @app.route('/')
    def home():
        return render_template('index.html')

    # Página de games
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

    # Página de consoles
    @app.route('/consoles')
    def consoles():
        return render_template(
            'consoles.html',
            nome="Nintendo Switch",
            lançamento=1969,
            marca="Nintendo",
            consoles=['PS4', 'Xbox', 'Nintendo Switch', 'PS5', 'PS1']
        )

    # Cadastro simples de games
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

    # Estoque de jogos
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

    # Editar jogo
    @app.route('/editar_jogos/<int:id>', methods=['GET', 'POST'])
    def editar_jogos(id):

        game = Game.query.get(id)

        if request.method == 'POST':

            dados_form = request.form.to_dict()

            game.titulo = dados_form['titulo']
            game.ano = dados_form['ano']
            game.categoria = dados_form['categoria']
            game.plataforma = dados_form['plataforma']
            game.preco = dados_form['preco']
            game.quantidade = dados_form['quantidade']

            db.session.commit()

            return redirect(url_for('estoque_jogos'))

        return render_template(
            'editar_jogos.html',
            game=game
        )

    # Cadastro de usuário
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():

        if request.method == 'POST':

            email = request.form['email']
            senha = request.form['senha']
            
            usuario = Usuario.query.filter_by(email=email).first()
            
            if usuario:
                msg = Markup("Usuário já cadastrado. Faça o <a href='/login'>login</a>")
                flash(msg, 'danger')
                return redirect(url_for('cadastro'))

            senha_criptografada = generate_password_hash(
                senha,
                method='scrypt'
            )

            novo_usuario = Usuario(
                email=email,
                senha=senha_criptografada
            )

            db.session.add(novo_usuario)
            db.session.commit()
            
            msgCad = Markup("Cadastro realizado com sucesso! Faça o <a href='/login'>login</a>")
            flash(msgCad, 'succes')

            return redirect(url_for('cadastro'))

        return render_template('cadastro.html')

    # Login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return "Bem vindo à página de login!"

    # Deletar jogo
    @app.route('/estoque_jogos/delete/<int:id>')
    def deletar_jogo(id):

        game = Game.query.get(id)

        if game:
            db.session.delete(game)
            db.session.commit()

        return redirect(url_for('estoque_jogos'))

    # Estoque de consoles
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

    # Deletar console
    @app.route('/estoque_consoles/delete/<int:id>')
    def deletar_console(id):

        console = Console.query.get(id)

        if console:
            db.session.delete(console)
            db.session.commit()

        return redirect(url_for('estoque_consoles'))