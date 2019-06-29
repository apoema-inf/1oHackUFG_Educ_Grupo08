from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from io import BytesIO
import http.client

class Request(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        string =json.loads(body)
        payload = "{}"
        response.write(b'POST errado')
        response.write(data)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 80), Request)
httpd.serve_forever()