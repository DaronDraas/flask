from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def first():
    return render_template("index.html")

@app.route('/<int:i>')
def divide(i):
    return render_template("index_1.html", i=i)

@app.route('/<int:j>/<int:i>')
def bonus_color(j, i):
    return render_template("index_2.html", j=j, i=i)

if __name__=="__main__":
    app.run(debug=True)