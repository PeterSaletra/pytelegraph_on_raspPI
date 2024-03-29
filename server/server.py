from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import cgi
import json

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['Content-Type'])

        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))

        with open('messages.txt', '+a') as file:
            file.write(data["word"] + "\n")
        
        self.protocol_verion = "HTTP/0.9"
        self.send_response(201)
        self.flush_headers()

    def do_GET(self):
        self.protocol_veriosn = "HTTP/0.9"
        self.send_response(200)
        self.flush_headers()
    

def main():
    '''
    Setsup Server.
    '''
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print("Server working correctly")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
