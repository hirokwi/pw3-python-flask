from flask import render_template, request, redirect, url_for


def init_app(app):

    listaGames = [
        {"titulo": "CS-GO", "ano": 2012, "categoria": "FPS online"}
    ]

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        titulo = "Warframe"
        ano = 1999
        categoria = "RPG"

        jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antonio']

        game = {
            "titulo": "Warframe",
            "ano": 1999,
            "categoria": "RPG"
        }

        return render_template(
            'games.html',
            titulo=titulo,
            ano=ano,
            categoria=categoria,
            jogadores=jogadores,
            game=game
        )

    @app.route('/consoles')
    def consoles():
        nome = "Nintendo Switch"
        lançamento = 1969
        marca = "Nintendo"

        consoles = ['PS4', 'Xbox', 'Nintendo Switch', 'PS5', 'PS1']

        return render_template(
            'consoles.html',
            nome=nome,
            lançamento=lançamento,
            marca=marca,
            consoles=consoles
        )

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        # verficando se o método da requisição é POSt
        if request.method == 'POST':
            # recebendo os dados do formulário e gravando na lista
            listaGames.append({'titulo' : request.form.get('titulo'), 'ano': request.form.get('ano'), 'categoria' : request.form.get('categoria')})
            # metodo append() adiciona valores a lista
            
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html', listaGames = listaGames)