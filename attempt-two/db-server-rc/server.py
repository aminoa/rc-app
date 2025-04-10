# Runs a server that is accessible on http://localhost:4000/. 
# When your server receives a request on http://localhost:4000/set?somekey=somevalue 
# it should store the passed key and value in memory. 
# When it receives a request on http://localhost:4000/get?key=somekey 
# it should return the value stored at somekey.

# TODO: save data to a file, make it performant

from flask import Flask, request

app = Flask(__name__)
db = {}

@app.route('/set', methods=['GET'])
def set():
    if len(request.args) != 1:
        return "Invalid Request: ", 400

    key, value = list(request.args.items())[0]

    if not key or not value:
        return "Invalid Request: Both key and value must be provided.", 400

    db[key] = value
    return f"Stored {key} = {value}"

@app.route('/get', methods=['GET'])
def get():
    key = request.args.get('key')

    if not key:
        return "Error: Missing 'key' parameter.", 404
    if key not in db:
        return "Error: Key not found.", 404

    return db[key]

if __name__ == '__main__':
    app.run(port=4000)