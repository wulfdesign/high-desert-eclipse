import http.server
import socketserver
import webbrowser
import sys
import os

PORT = 3008

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    try:
        with socketserver.ThreadingTCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}/index.html"
            print(f"==================================================")
            print(f"  🕶️ High Desert Eclipse Multi-Threaded WebXR Server")
            print(f"  Serving at: {url}")
            print(f"==================================================")
            webbrowser.open(url)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutting down cleanly.")
        sys.exit(0)

if __name__ == "__main__":
    run_server()
