import http.server
import socketserver
import datetime
import os

PORT = 443
INCOMING_DIR = "/home/ec2-user/datashield/incoming"
LOG_FILE = "/home/ec2-user/datashield/logs/collector-ingest.log"

class IngestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length)
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"{INCOMING_DIR}/data_{timestamp}.txt"

        with open(filename, 'wb') as f:
            f.write(body)

        with open(LOG_FILE, 'a') as log:
            log.write(f"{datetime.datetime.now()} Received file: {filename} ({length} bytes)\n")

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(b'{"status":"received"}')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(("", PORT), IngestHandler) as httpd:
    print(f"Collector ingestion server running on port {PORT}")
    httpd.serve_forever()
