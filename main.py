import random
from flask import Flask

app = Flask(__name__)

datos = [
    "Casi todo el dinero que existe no son billetes ni monedas físicas, sino números en discos duros de bancos.",
    "Tu celular es más potente que la computadora que llevó al hombre a la Luna.",
    "El 90% del dinero del mundo solo existe en computadoras, no en billetes.",
    "La primera página web de la historia todavía está en línea.",
    "Aproximadamente el 50% de la población mundial nunca ha hecho una llamada telefónica.",
    "Google procesa más de 3.5 mil millones de búsquedas por día.",
    "El nombre 'Google' proviene del término matemático 'Googol', que es un 1 seguido de 100 ceros.",
    "Se suben más de 500 horas de video a YouTube cada minuto.",
    "El primer mouse de computadora fue hecho de madera.",
    "El 80% de los correos electrónicos enviados diariamente son spam.",
    "Existen más de 1,800 millones de sitios web en el mundo, pero menos de 200 millones están activos.",
    "La primera cámara fotográfica tardaba 8 horas en tomar una sola foto.",
    "El código fuente de los navegadores modernos tiene millones de líneas de código."
]

@app.route("/")
def hello_world():
    return '''
        <h1>¡Bienvenido a la página de datos curiosos!</h1>
        <p>Toda la vara tecnológica la encuentras aquí.</p>
        <a href="/datos">Ver un dato aleatorio</a>
    '''

@app.route("/datos")
def get_datos():
    return f'''
        <p>{random.choice(datos)}</p>
        <br>
        <a href="/">Volver al inicio</a>
    '''
      
if __name__ == "__main__":
    app.run(debug=True)