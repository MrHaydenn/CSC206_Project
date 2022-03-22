from flask import Flask, render_template, request

from PrimesProgram import primes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def recieveData():
    variable = request.form['variable']
    return variable, primes











if __name__== "__main__":
    app.run()


