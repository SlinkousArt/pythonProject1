# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import mimetypes
import time

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        filepath = self.path
        mimetype, _ = mimetypes.guess_type(filepath)
        self.send_header("Content-type", mimetype)
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>test</title><style>html{font-family:monospace; color:green; background:black;}</style></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Never Gonna Give You Up, Never gonna let you down, never gonna run around and</p>"
                               "<p>get rickrolled lol</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
