# Comentário em Python
# Importando o Flask na aplicação
from flask import Flask, render_template # renderiza as páginas html
from controllers import routes

# Carregando o Flask em uma variável
# Declarando variável no Python
app = Flask(__name__, template_folder='views')

# __name__ é uma variável de ambiente do Python que tem o nome do módulo atual.

routes.init_app(app)

# Iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True) # ligando o modo de depuração (reinicia automatico)
    # Verificando se oapp.py for o arquivo principal ele inicia o servidor.