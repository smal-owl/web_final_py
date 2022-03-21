from flask import Flask
from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"

@app.route('/image_mars')
def ddd():
    return f'''<h1>Жди нас, Марс!<h1><img src="{url_for('static', filename='photo.png')}" 
           alt="здесь должна была быть картинка, но не нашлась"><h3>Вот она какая, красная планета<h3>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')