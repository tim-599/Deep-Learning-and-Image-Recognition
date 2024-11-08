import pandas as pd
import numpy as np
import json
import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
from os import listdir

# define Flask_app
app = Flask(__name__)
CORS(app)

@app.route("/API_Router", methods = ["POST", "GET"])
def API_test():
    #取得請求資料
    req_data = request.get_json(force = True)
    #取得請求IP
    print(request.remote_addr)

    #資料處理



    
    #建構回傳json檔案
    rep = {
            "State_Code":200,
        }
    #回傳結果 把rep變成json檔
    return jsonify(rep)



if __name__ == '__main__':
	app.run(host='127.0.0.1', port=6666, debug=True)
