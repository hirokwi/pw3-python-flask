from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/list')
def list():
    return render_template('list.html')



if __name__ == '__main__':
    app.run(debug=True)