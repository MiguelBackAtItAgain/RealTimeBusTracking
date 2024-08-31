import urllib.request
import mysql.connector
import json
import os

db = mysql.connector.connect(
    host='localhost',
    user='root',
    port='3306',
    password=os.getenv('MYSQL_PASSWORD'),
    database='MBTAdb'
)

class BusRoute:

    def __init__(self):
        pass

    def read(self):
        url = "https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip"
        response = urllib.request.urlopen(url).read()
        data = json.loads(response)
        data_list = data.get('data', [])
        filtered_data = [
            {
                "id": vehicle.get('id'),
                "latitude": vehicle["attributes"].get('latitude'),
                "longitude": vehicle["attributes"].get('longitude')
            }
            for vehicle in data_list
        ]
        return filtered_data

    def write(self, id, ln, lt, time):
        cursor = db.cursor()
        script = 'INSERT INTO mbta_buses (id, longitude, latitude, created) VALUES (%s, %s, %s, %s)'
        cursor.execute(script, (id, ln, lt, time))
        db.commit()
        cursor.close()
