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

@app.route('/noticia2')
def noticia2():
    return render_template('noticia2.html')

@app.route('/noticia3')
def noticia3():
    return render_template('noticia3.html')

@app.route('/noticia4')
def noticia4():
    return render_template('noticia4.html')

@app.route('/noticia5')
def noticia5():
    return render_template('noticia5.html')

@app.route('/noticia6')
def noticia6():
    return render_template('noticia6.html')