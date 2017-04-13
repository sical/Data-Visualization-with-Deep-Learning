from flask import Flask, render_template, request
import Request_Use as ru

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
    print(result)
    return ru.askbasicurl(result)


@app.route('/tensorflow')
def tensorflow():
    return render_template('tensorflow.html')


if __name__ == '__main__':
    app.run()
