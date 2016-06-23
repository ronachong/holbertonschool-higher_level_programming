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
# import SimpleHTTPServer as http <-- this would use a filesystem instead of code?
import mysql.connector as mysql

# create handler class for http server (which only handles gets requests)
class GET_handler(Handler):

    def get_params(self):
        params = self.path.split('/')[3::]
        return params

    def do_GET:
        self.send_response(200)                     # provide response code for no errors?
        self.send_header('Content-type', 'json')    # specify the type of response served as header? not sure
        self.end_headers()

        params = self.get_params()
        if len(params) == 1 and params[0] == 'tvshows':
            response = get_tvshows()

        self.wfile.write(response)

# create http server
PORT = 9898
try:
    httpd = HTTPServer(('', PORT), Get_handler)
    print 'server started...'
    httpd.serve_forever
except KeyboardInterrupt:
    print '^C: shutting down server'
    server.socket.close()


# helper methods defined here
def get_kvpair(cursor, id, table, attribute):
    query = ("SELECT " +  attribute + " FROM " + table + " WHERE id=" + str(id) + ";")
    cursor.execute(query)
    value = cursor.fetchall()[0][0]
    return (attribute, value)

def get_tvshows
    # make a master list to contain the json struct
    mlist = []
    table_attrs = { 'TVShow': ['id', 'name', 'poster'],
                    'Network': ['id', 'name'],
                    'TVShowActor': ['tvshow_id', 'actor_id'],
                    'Actor': ['id', 'name'],
                    'TVShowGenre': ['tvshow_id', 'genre_id'],
                    'Genre': ['id', 'name'],
                    'Season': ['id', 'number', 'tvshow_id'],
                    'Episode': ['id', 'name', 'number', 'overview', 'season_id']   }
    attr_list = table_attrs['TVShow']
    cnx = mysql.connect(user='student',
                        password='aLQQLXGQp2rJ4Wy5',
                        host='173.246.108.142',
                        database='Project_169')
    cursor = cnx.cursor()
    query = ("SELECT id from TVShow;")

    cursor.execute(query)
    for record in cursor.fetchall():
        id = record[0]
        # run through attributes and create dict for record, using list mapping
        dict_list = []
        for attribute in attr_list:
            value = get_kvpair(cursor, id, urlarg, attribute)
            dict_list.append(value)
        rec_dict = dict(dict_list)
        mlist.append(rec_dict)

    cnx.close()
    return mlist
