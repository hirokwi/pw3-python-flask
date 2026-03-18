# Comentário em Python
# Importando o Flask na aplicação
from flask import Flask, render_template # renderiza as páginas html


# Carregando o Flask em uma variável
# Declarando variável no Python
app = Flask(__name__, template_folder='views')

# __name__ é uma variável de ambiente do Python que tem o nome do módulo atual.

# Criando a rota principal do site
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
    
    return render_template('games.html',
    titulo = titulo,
    ano = ano,
    categoria = categoria,
    jogadores = jogadores,)




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


# Iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True) # ligando o modo de depuração (reinicia automatico)
    # Verificando se oapp.py for o arquivo principal ele inicia o servidor.