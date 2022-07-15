from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def tabla():
    users = [
   {'nombre' : 'Michael', 'apellido' : 'Choi'},
   {'nombre' : 'John', 'apellido' : 'Supsupin'},
   {'nombre' : 'Mark', 'apellido' : 'Guillen'},
   {'nombre' : 'KB', 'apellido' : 'Tonel'}
]
    return render_template("index.html", users=users)


if __name__=="__main__":
    app.run(debug=True)