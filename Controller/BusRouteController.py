from Services.BusRouteService import BusRoute
from datetime import datetime

busObj = BusRoute()

class bus:

    def __init__(self):
        pass

    def read(self):
        return busObj.read()
    
    def write(self):
        bus_data = self.read()

        for vehicle in bus_data:
            busObj.write(vehicle.get('id'), vehicle.get('latitude'), vehicle.get('longitude'), datetime.now())
