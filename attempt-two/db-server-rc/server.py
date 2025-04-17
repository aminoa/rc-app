# Runs a server that is accessible on http://localhost:4000/. 
# When your server receives a request on http://localhost:4000/set?somekey=somevalue 
# it should store the passed key and value in memory. 
# When it receives a request on http://localhost:4000/get?key=somekey 
# it should return the value stored at somekey.

# Edit 1: Rewrote server to use built-in HTTP library rather than Flask

# TODO: save data to a file, make it performant

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

store = {}

class RequestHandler(BaseHTTPRequestHandler):

    def get(self, query_params):
        """Retrieve the data with key"""
        key = query_params.get('key', [None])[0]
        if not key or key not in store:
            self.send_error(400, "Invalid Request: Missing 'key' Parameter or key not found")
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/text/plain')
        self.end_headers()
        self.wfile.write(f"Value: {store[key]}".encode())

    def set(self, query_params):
        # make sure only one parameter is sent
        if len(query_params) != 1:
            self.send_error(400, "Invalid Request: Send exactly one key and value")
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/text/plain')
        self.end_headers()

        # this should only have one key
        for key in query_params:
            value = query_params[key]
            store[key] = value
            self.wfile.write(f"{key} = {value}\n".encode())


    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        match parsed_url.path:
            case '/get':
                self.get(query_params)
            case '/set':
                self.set(query_params)
            case _:
                self.send_error(400, "Invalid Request")
                self.end_headers()

def main():
    httpd = HTTPServer(('localhost', 4000), RequestHandler)
    print("Running server on http://localhost:4000")
    httpd.serve_forever()

if __name__ == '__main__':
    main()