from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "1312"

@app.route('/')
def countbase():
    if "visits" in session:
        session['visits'] +=1
    else:
        print("key does not exist")
        session['visits'] = 1
    return render_template("index.html")

@app.route('/count')
def count():
    session['visits'] += 1
    return redirect('/')

@app.route('/reset')
def reseteo():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)