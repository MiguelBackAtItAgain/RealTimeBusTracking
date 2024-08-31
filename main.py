from flask_cors import CORS
from flask import Flask, render_template
from Controller.BusRouteController import bus
import os

app = Flask(__name__)
CORS(app)
busObj = bus()

@app.route('/')
def index():
    token = os.getenv('MAPBOX_ACCESS_TOKEN')
    return render_template('index.html', mapbox_token=token)

def create():
    busObj.write()

@app.route('/getTransportData', methods=['GET', 'POST'])
def read():
    create()
    return busObj.read()

if __name__ == '__main__':
    app.run(debug=True, port=3000)