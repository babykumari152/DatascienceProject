from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd
from flask import Blueprint, render_template

gets = Blueprint('gets', __name__)

#app = Flask(__name__)

@gets.route('/get', methods=["GET"])
def get():

    lis = pd.read_csv('db.csv')
            #print(lis)
    lm=lis.to_dict('index')
            #print(lm)
    print("abc")
    s = list(lis.to_dict('index').values())
    return jsonify(s)
#if __name__== '__main__':
   # app.run(debug=True,port=5000)
