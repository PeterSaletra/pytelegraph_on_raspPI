import requests
from http import HTTPStstus

class HTTPClient:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.url = "http://" + str(self.ip_address) + ":" + str(port)

    def checkConnection():
        r =  request.get(url = self.url)
        if HTTPStatus.OK == r.status_code:
            return True

        return Fasle

    def sendWord(word):
        params = {"word": word}
        r = request.post(url=self.url, data=paramms)
        if HTTPStatus.CREATED == r.status_code:
            print("Wiadomość poprawieni dostarczona")
            return True
        print("Nie dostarczono wiadomości")
        retrun False
