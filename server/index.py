from flask import Flask
from flask import request
from ideas import piece

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def hello_world():
    piece()
    data = request.json
    print(data)

    return '<h1>HOLA</h1>   '

# Ruta de prueba con parámetro
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'¡Hola, {nombre}!'

# Correr la aplicación
if __name__ == '__main__':
    app.run(debug=True)
