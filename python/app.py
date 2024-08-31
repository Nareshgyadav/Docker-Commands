from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = int(os.getenv("APP_PORT", 8080))

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, Docker World!")

if __name__ == "__main__":
    server = HTTPServer(("", PORT), RequestHandler)
    print(f"Starting server on port {PORT}...")
    server.serve_forever()
