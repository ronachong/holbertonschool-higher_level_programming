'''
6-main.py creates a simple http server listening to port 9898 of its host.
The http server expects GET requests in the following format:
`curl 'http://<ip of host>:9898/<url arg 1>[/<url arg 2>][further option url args]'`
In response to a GET request, the server looks at each url arg and returns the
corresponding json values from the database Project 169.
In other words, the server acts as a JSON API for the database Project 169.
'''

# modules
from BaseHTTPServer import BaseHTTPRequestHandler as Handler, HTTPServer
from helper import *

# create handler class for http server (which only handles gets requests)
class GET_handler(Handler):

    def get_params(self):
        params = self.path.split('/')[1::]
        return params

    def do_GET(self):
        #self.send_response(200)                     # provide response code for no errors?
        #self.send_header('Content-type', 'json')    # specify the type of response served as header? not sure
        #self.end_headers()

        params = self.get_params()
        if len(params) == 1 and params[0] == 'tvshows':
            response = get_tvshows()
        if len(params) == 2:
            response = get_tvshow_detail(params[1])

        self.wfile.write(response)

# create http server
def main():
    PORT = 9898
    try:
        httpd = HTTPServer(('', PORT), GET_handler)
        print 'HTTP Server Running...........'
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '^C: shutting down server'
        httpd.socket.close()

if __name__ == '__main__':
    # execute only if run as a script
    main()
