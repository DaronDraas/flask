from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'
@app.route('/cambioruta/<string:nombre>')
def ruta(nombre):
    return render_template("Paquetejinja.html",nombre=nombre)

@app.route('/cambioruta')
def saludo():
    return render_template("index.html")
      # Devuelve la cadena '¡Hola Mundo!' como respuesta
if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
