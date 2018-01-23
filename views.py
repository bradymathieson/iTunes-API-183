from flask import Flask, request, jsonify
from helpers import *
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    return "nothin' here"

@app.route('/get_artist_id', methods=["GET", "POST"])
def gid():
    if not len(request.args):
        return "bad!"
    if request.args['name']:
        name = convert_string_for_req(request.args['name'])
        r = requests.get("http://itunes.apple.com/search?type=music&limit=1&term={}".format(name))
        try:
            return jsonify({'artist': convert_string_from_req(name), 'id': r.json()['results'][0]['artistId']})
        except:
            return "no match or invalid format"
        
    else:
        return "bad!"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

