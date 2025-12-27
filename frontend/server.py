# Author: Daksha009
# Repo: https://github.com/Daksha009/AirSense-Guardian.git

"""
Simple HTTP server to serve the frontend HTML file
"""
import http.server
import socketserver
import os
import sys

PORT = 3000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        # Serve index.html for root path and all routes
        if self.path == '/' or self.path == '/index.html' or not self.path.startswith('/api'):
            # Serve index.html for all non-API routes (SPA support)
            self.path = '/index.html'
        return super().do_GET()
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Frontend server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

