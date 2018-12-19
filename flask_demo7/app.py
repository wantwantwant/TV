# bootstrap
from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo1')
def demo1():
    return render_template('demo1.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
