from flask import render_template


def init_app(app):

  from flask import render_template


# criando a função para receber o flask (app)
def init_app(app):
    # a partir daqui virão as rotas
    
    @app.route('/')
    # Def serve para criar funções no Python
    def home():
        return render_template('index.html')


    @app.route('/games')
    def games():

        titulo = "Warframe"
        ano = 1999
        categoria = "RPG"    
        jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antonio']
        
        game = {
        "titulo" : "Warframe",
        "ano" : 1999,
        "categoria" : "RPG"}
        
        return render_template('games.html',
        titulo = titulo,
        ano = ano,
        categoria = categoria,
        jogadores = jogadores,
        game = game,)


    @app.route('/consoles')
    def consoles():
        nome = "Nintendo Switch"
        lançamento = 1969
        marca = "Nintendo"
        
        consoles = ['PS4', 'Xbox', 'Nintendo Switch', 'PS5', 'PS1']
        
        return render_template('consoles.html',
        nome = nome,
        lançamento = lançamento,
        marca = marca,
        consoles = consoles,)