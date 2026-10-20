import os
import socket
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000
SHARED_DIR = "SharedFiles"
INDEX_FILE = "index.html"

if not os.path.exists(SHARED_DIR):
    os.makedirs(SHARED_DIR)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class ThreadedFileShareHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/upload':
            filename = self.headers.get('File-Name', 'unknown_file')
            filename = urllib.parse.unquote(filename)
            file_length = int(self.headers.get('Content-Length', 0))
            
            filepath = os.path.join(SHARED_DIR, filename)
            
            with open(filepath, 'wb') as f:
                chunk_size = 8192
                while file_length > 0:
                    chunk = self.rfile.read(min(chunk_size, file_length))
                    if not chunk:
                        break
                    f.write(chunk)
                    file_length -= len(chunk)
                    
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Upload Complete")
        else:
            self.send_error(404, "Not Found")

    def do_GET(self):
        if self.path == '/list_files':
            import json
            files = os.listdir(SHARED_DIR)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(files).encode('utf-8'))
            
        elif self.path.startswith('/download/'):
            filename = urllib.parse.unquote(self.path.split('/download/')[1])
            filepath = os.path.join(SHARED_DIR, filename)
            
            if os.path.exists(filepath):
                self.send_response(200)
                self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
                self.send_header('Content-type', 'application/octet-stream')
                self.end_headers()
                with open(filepath, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "File not found")
        else:
            super().do_GET()

if __name__ == "__main__":
    local_ip = get_local_ip()
    hub_url = f"http://{local_ip}:{PORT}/{INDEX_FILE}"
    
    print(f"\n🚀 UniShare Hub running!")
    print(f"📁 Saving files to: {os.path.abspath(SHARED_DIR)}")
    print(f"🌐 Laptop Link: http://localhost:{PORT}/{INDEX_FILE}")
    print(f"📡 Wi-Fi Link:  {hub_url}")
    
    try:
        import qrcode
        qr = qrcode.QRCode()
        qr.add_data(hub_url)
        qr.make(fit=True)
        print("\n📱 Scan this QR code to join the Hub directly:\n")
        qr.print_ascii(invert=True) 
    except ImportError:
        print("\n[!] QR code disabled. Run 'pip install qrcode' to see it here in the terminal.\n")

    with ThreadingHTTPServer(("0.0.0.0", PORT), ThreadedFileShareHandler) as httpd:
        httpd.serve_forever()
