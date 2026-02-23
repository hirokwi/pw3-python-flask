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
    return render_template('games.html')

@app.route('/consoles')
def consoles():
    return render_template('consoles.html')


# Iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True) # ligando o modo de depuração (reinicia automatico)
    # Verificando se oapp.py for o arquivo principal ele inicia o servidor.