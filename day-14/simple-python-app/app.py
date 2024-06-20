from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloo():
    return 'Helloo, world!'

if __name__ == '__main__':
   app.run()

