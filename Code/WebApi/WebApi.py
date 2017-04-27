from flask import Flask, render_template, request
import Request_Use as ru
import Reload as rl
import wget
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


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


@app.route('/tensorflowlocal', methods=['POST'])
def tensorflowlocal():
    result = request.files['local']
    type = str(result.filename).split('.')
    type = type[len(type) - 1]
    if type == 'png':
        return rl.go('png', result)
    else:
        return rl.go('jpg', result)


@app.route('/tensorflowurl', methods=['POST'])
def tensorflowurl():
    result = request.form['url']
    file = wget.download(result)
    name = wget.detect_filename(result)
    temp = name.split('.')

    ext = str(temp[len(temp) - 1])
    if ext == 'png':
        pred = rl.go('png', file, os.path.join(os.getcwd(), name))
    else:
        pred = rl.go('jpg', file, os.path.join(os.getcwd(), name))

    return pred

@app.route('/tensorflowblob', methods=['POST'])
def tensorflowblob():
    result = request.files['local']
    print(result.filename)
    return rl.go('png',result)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
