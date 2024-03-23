import requests
from http import HTTPStstus

Class HTTPClient:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.url = "http://" + str(self.ip_address) + ":" + str(port)

    def checkConnection():
        if HTTPStatus.OK request.get(url = self.url):
            return true

        return fasle

