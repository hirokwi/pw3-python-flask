from flask import Flask
from controllers.routes import init_app

app = Flask(__name__, template_folder='views', static_folder='static')

init_app(app)

if __name__ == '__main__':
    app.run(debug=True)