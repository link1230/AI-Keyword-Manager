"""PromptManager — native desktop app via Edge WebView2"""
import os, sys, json, http.server, threading, socket, ctypes
from ctypes import wintypes

# Find a free port
def free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0)); p = s.getsockname()[1]; s.close(); return p

PORT = free_port()
HOST = '127.0.0.1'

# --- HTTP server ---
class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
        '.html':'text/html; charset=utf-8','.json':'application/json; charset=utf-8'}
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.path = '/preview/index.html'
        return super().do_GET()
    def log_message(self, *a): pass

def get_dir():
    return sys._MEIPASS if getattr(sys,'frozen',False) else os.path.dirname(os.path.abspath(__file__))

def start_server():
    os.chdir(get_dir())
    srv = http.server.HTTPServer((HOST, PORT), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv

# --- Native window via Edge WebView2 ---
# Use ctypes to call Windows WebView2 through a small JavaScript bridge
# We create an HTA-like solution: write a temp .htm that hosts WebView2
# Then launch it with msedge (Edge is on every Windows 10/11)

import tempfile, subprocess

def create_bridge_html():
    """Create a temporary HTML that loads our app in full-screen WebView2"""
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<title>PromptManager</title>
<style>body{{margin:0;overflow:hidden}} webview{{width:100vw;height:100vh;border:none}}</style>
</head><body>
<webview src="http://{HOST}:{PORT}" style="width:100vw;height:100vh"></webview>
<script>
const wv=document.querySelector('webview');
wv.addEventListener('newwindow',e=>{{ e.preventDefault(); wv.loadURL(e.targetUrl); }});
</script></body></html>'''

# --- Launch method ---
def launch_browser():
    """Use Edge with app mode for a native window feel"""
    edge = None
    for p in [r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
              r'C:\Program Files\Microsoft\Edge\Application\msedge.exe']:
        if os.path.exists(p): edge = p; break
    if not edge:
        import webbrowser; webbrowser.open(f'http://{HOST}:{PORT}'); return
    # Edge app mode: no address bar, no toolbar — looks like native app
    subprocess.Popen([edge, f'--app=http://{HOST}:{PORT}', '--new-window',
                      '--window-size=1280,820', '--disable-extensions'],
                     creationflags=subprocess.CREATE_NO_WINDOW if sys.platform=='win32' else 0)

def main():
    srv = start_server()
    launch_browser()
    print(f'\n  PromptManager running on port {PORT}\n  Press Enter to exit...\n')
    try: input()
    except: pass
    srv.shutdown()

if __name__ == '__main__':
    main()
