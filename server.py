import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("🚀 Omi Website running at http://localhost:8000")
    httpd.serve_forever()
