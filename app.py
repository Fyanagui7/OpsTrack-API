from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
    int a =2
    int b =2
    result = (a+b)
    return result


if __name__ == '__main__':
    app.run()

#comentario de exemplo1