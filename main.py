from http.server import HTTPServer, BaseHTTPRequestHandler,SimpleHTTPRequestHandler
from jinja2 import Environment, PackageLoader,select_autoescape
from photo import photo_mas



class CustomHandler(SimpleHTTPRequestHandler):
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    def do_GET(self):
        if self.path.startswith('/media/'):
            super().do_GET()
        elif self.path == '/':
            self.render_index()




    def render_index(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        body=self.env.get_template('index.html').render(photo_mas=photo_mas)
        self.wfile.write(body.encode('utf-8'))




def run(server_class=HTTPServer,handler_class=BaseHTTPRequestHandler):

    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("[+] Server starting")
    httpd.serve_forever()

if __name__=="__main__":
    run(handler_class=CustomHandler)
