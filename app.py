from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#funcion principal
if __name__ == '__main__':
    #cargar el objeto principal a todas las interfaces de red en el puerto 80
    app.run(host='0.0.0.0',port=8000)
