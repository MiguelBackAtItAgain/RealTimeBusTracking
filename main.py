import urllib.request
from flask_cors import CORS
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)

def get_transport_data():
    url = "https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip"
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data

@app.route('/getTransportData', methods=['POST'])
def webhook():
    all_data = get_transport_data()
    data_list = all_data.get('data', [])
    filtered_data = [
        {
            "id": vehicle.get('id'),
            "latitude": vehicle["attributes"].get('latitude'),
            "longitude": vehicle["attributes"].get('longitude')
        }
        for vehicle in data_list
    ]
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
