from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-length'])
        post_data = self.rfile.read(content_length)
        parsed_data = urllib.parse.parse_qs(post_data.decode())
        message = parsed_data.get('word', [''])[0]

        with open('messages.txt', '+a') as file:
            file.write(message + "\n")

        self.send_response(201)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Wiadomosc poprawieni zapiasana")

    def do_GET(self):
        self.send_response(200)
    

def main():
    '''
    Setsup Server.
    '''
    server_address = ('192.170.1.133', 8000)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print("Server working correctly")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
