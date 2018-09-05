#Command line:
#   cd {path_to_directory}/ex2
#   export FLASK_APP=restapi.py
#   flask run --port=5300
#   
#########################
import os
from flask import Flask, request, json, jsonify, Response
from flask_cors import CORS
import upjson as pkg


app = Flask(__name__)
CORS(app)

@app.route('/api/points', methods=['GET', 'POST'])
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT,'static', 'points.json')
    response = pkg.main()
    jdata = json.load(open(json_url))
    return jsonify(jdata)

#app.run(port=5300)

if __name__ == '__main__':
    app.run(debug=True)

