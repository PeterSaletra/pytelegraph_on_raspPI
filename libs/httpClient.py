import requests
from http import HTTPStatus

class HTTPClient:
    def __init__(self, ip_address: str, port: int):
        self.ip_address = ip_address
        self.port = port
        self.url = "http://" + self.ip_address + ":" + str(port)

    def checkConnection(self) -> bool:
        '''
        Checks connection to HTTP Server.

        :return bool: If connection is OK returns True else returns False
        '''
        r = requests.get(url = self.url)
        if HTTPStatus.OK == r.status_code:
            return True

        return False

    def sendWord(self, word: str) -> bool:
        '''
        Send word over request into server with word transleted from morse code.
        :param str word: Tranlated word from morse code
        :return bool: If request was corretly handles by server returns True else Return False
        '''

        params = {"word": word}
        r = requests.post(url=self.url, data=params)
        if HTTPStatus.CREATED == r.status_code:
            print("Message was send correctly")
            return True
        print("Error occurred")
        return False
