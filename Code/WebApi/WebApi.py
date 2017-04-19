from flask import Flask, render_template, request
import Request_Use as ru
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('nanonets.html')


@app.route('/nanonets')
def nanonets():
    return render_template('nanonets.html')


@app.route('/nanonetsurl', methods=['POST'])
def nanonetsurl():
    result = request.form['url']
    return ru.askbasicurl(result)


@app.route('/nanonetslocal', methods=['POST'])
def nanonetslocal():
    result = request.files['local']
    return ru.askbasiclocal(result)


@app.route('/tensorflow')
def tensorflow():
    return render_template('tensorflow.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
