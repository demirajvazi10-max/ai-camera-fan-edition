import http.server
import socketserver
import socket
import os
import sys
import webbrowser
from pathlib import Path

# =============================================
# AI Camera — Local server for testing
# Double-click this file to run it
# =============================================

PORT = 8080

# Move into the folder where this Python file lives
os.chdir(Path(__file__).parent)

# Find the local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

local_ip = get_local_ip()

print("=" * 50)
print("   AI Camera — Local server")
print("=" * 50)
print()
print(f"  On this computer:  http://localhost:{PORT}")
print(f"  On your phone (WiFi): http://{local_ip}:{PORT}")
print()
print("  IMPORTANT: your phone and computer must be")
print("  on the same WiFi network!")
print()
print("  To stop the server: press Ctrl+C")
print("=" * 50)
print()

# Automatically open the browser on this computer
webbrowser.open(f"http://localhost:{PORT}")

# Start the server
handler = http.server.SimpleHTTPRequestHandler

# Silence noisy logs
class QuietHandler(handler):
    def log_message(self, format, *args):
        # Only show errors
        if args[1] not in ('200', '304'):
            print(f"  [{args[1]}] {args[0]}")

try:
    with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print()
    print("  Server stopped.")
except OSError:
    print(f"  ERROR: Port {PORT} is already in use.")
    print(f"  Try changing PORT to 8081 in this file.")
    input("  Press Enter to exit...")
    sys.exit(1)
