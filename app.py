from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! CI/CD works!'

if __name__ == '__main__':
    app.run()   
# test code build
