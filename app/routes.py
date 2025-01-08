from app import app
from flask import render_template

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cancelamento')
def cancelamento():
    return render_template('cancelamento.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/noticias')
def noticia():
    return render_template('noticias.html')

@app.route('/noticia1')
def noticia1():
    return render_template('noticia1.html')