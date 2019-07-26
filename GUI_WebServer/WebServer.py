from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

class WebServer:
    def __init__(self, address = "localhost", port = 60000):
            self.__serverAddress = address
            self.__serverPort = port

    def runServer(self):
        serverInfo = (self.__serverAddress, self.__serverPort)
        Handler = self.httpRequest()
        with socketserver.TCPServer(serverInfo, Handler) as httpd:
            httpd.serve_forever()

    class httpRequest(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = '/index.html'
            try:
                fileToOpen = open(self.path[1:]).read()
                self.send_response(200)
            except:
                fileToOpen = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(fileToOpen, 'utf-8'))