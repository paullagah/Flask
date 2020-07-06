from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'HOWDY PARDNER!!!!!!!'

@app.route('/about')
def about():
    return ''

if __name__ == '__main__':
    app.run()
