from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/api/hello',methods=['GET'])

def start():
    return json.dumps({'code':'O'})

if __name__ == '__main__':

    app.run(host='0.0.0.0',port = 8080,debug=True)  #49.77.230.119