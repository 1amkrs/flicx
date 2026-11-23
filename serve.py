import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        # Resolve clean URLs to .html or /index.html
        path = self.path.split('?')[0]
        local_path = os.path.join(DIRECTORY, path.lstrip('/'))
        
        if not os.path.exists(local_path):
            if os.path.exists(local_path + '.html'):
                self.path = path + '.html'
            elif os.path.exists(os.path.join(local_path, 'index.html')):
                self.path = os.path.join(path, 'index.html').replace('\\', '/')
            elif path.startswith('/watch/'):
                watch_default = os.path.join(DIRECTORY, 'watch', 'avatar-fire-and-ash-2025', 'index.html')
                if os.path.exists(watch_default):
                    self.path = '/watch/avatar-fire-and-ash-2025/index.html'
        
        return super().do_GET()

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), SPAHandler) as httpd:
        print(f"Flicx Offline Server running at: http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
