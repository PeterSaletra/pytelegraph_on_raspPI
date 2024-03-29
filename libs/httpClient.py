import sys
import json
import http.client
from http import HTTPStatus

class HTTPClient:
    def __init__(self, ip_address: str, port: int):
        self.ip_address = ip_address
        self.port = port
        self.conn = http.client.HTTPConnection(self.ip_address, self.port)

    def checkConnection(self) -> bool:
        '''
        Checks connection to HTTP Server.

        :return bool: If connection is OK returns True else returns False
        '''
        try:
            self.conn.request("GET", "/")
            r = self.conn.getresponse()
            if HTTPStatus.OK == r.status:
                return True
        except Exception as e:
            print("Error occured:" + str(e))

        return False

    def sendWord(self, word: str) -> bool:
        '''
        Send word over request into server with word transleted from morse code.
        :param str word: Tranlated word from morse code
        :return bool: If request was corretly handles by server returns True else Return False
        '''
        try:
            params = json.dumps({"word": word})
            self.conn.request("POST", "/", body=params, headers={"Content-Type": "application/json"})
            r = self.conn.getresponse()
            if HTTPStatus.CREATED == r.status:
                print("Message was send correctly")
                return True
        except Exception as e:
            print("Error occurred:" + str(e))

        return False
