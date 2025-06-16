from flask import Flask, render_template # type: ignore
import requests


# creamos una instancia de la aplicacion Flask. __name__ le dice a Flask que este es el archivo principal
app = Flask(__name__)

# definimos una ruta principal y asociamos esa ruta con la funcion home()
@app.route('/')
def home():
    # URL de la API de Jolpica para obtener las carreras
    url = 'https://api.jolpi.ca/ergast/f1/current.json'
    
    try:
        # hacemos una solicitud GET a la API
        response = requests.get(url)
        # convertimos la respuesta JSON a un diccionario de Python
        data = response.json()
        
        # navegamos por la estructura del JSON hasta llegar al array con las carreras, y extraemos las carreras desde la estructura de la respuesta
        races = data['MRData']['RaceTable']['Races']
    
    except requests.exceptions.RequestException as err:
        races = []
        print(f"Error al obtener los datos: {err}")
    
    # Flask busca un archivo en la carpeta templates/ y lo renderiza como HTML
    return render_template('home.html', races=races)



@app.route('/drivers')
def drivers():
    url = "https://api.jolpi.ca/ergast/f1/current/drivers.json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        drivers = data['MRData']['DriverTable']['Drivers']
        
    except requests.exceptions.RequestException as err:
        drivers = []
        print(f"Error al obtener los pilotos:", err)
        
    return render_template('drivers.html', drivers=drivers)



@app.route('/constructors')
def constructors():
    url = "https://api.jolpi.ca/ergast/f1/current/constructors.json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        constructors = data['MRData']['ConstructorTable']['Constructors']
        
    except requests.exceptions.RequestException as err:
        constructors = []
        print(f"Error al obtener los constructores:", err)
        
    return render_template('constructors.html', constructors=constructors)
        


@app.route('/calendar')
def calendar():
    url = "https://api.jolpi.ca/ergast/f1/current.json"

    try:
        response = requests.get(url)
        data = response.json()
        
        races = data['MRData']['RaceTable']['Races']
        
    except requests.exceptions.RequestException as err:
        races = []
        print(f"Error al obtener el calendario: ", err)

    return render_template('calendar.html', races=races)



@app.route('/standings')
def standings():
    url = "https://api.jolpi.ca/ergast/f1/current/driverstandings.json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        standings_list = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        
    except requests.exceptions.RequestException as err:
        standings_list = []
        print(f"Error al obtener los standings: ", err)
        
    return render_template('standings.html', standings=standings_list)










# ejecutamos la aplicacion
if __name__ == '__main__':
    # inicia el servidor, con debug=True Flask recarga automaticamente si cambiamos el codigo y muestra errores mas detallados.
    app.run(debug=True) 
    
    