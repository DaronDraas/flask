from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "@polo57h"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resultado')
def resultado():
    return render_template("resultado.html")

@app.route('/process', methods=['POST'])
def process():
    session['nombre'] = request.form['nombre']
    session['ubicacion'] = request.form['ubicación']
    session['lenguaje'] = request.form['lenguaje']
    session['comentarios'] = request.form['comentarios']
    return redirect('resultado')

if __name__=="__main__":
    app.run(debug=True)