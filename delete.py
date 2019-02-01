from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd
from flask import Blueprint, render_template

deletes = Blueprint('deletes', __name__)


#app = Flask(__name__)
@deletes.route('/delete',methods=["DELETE"])
def dels():
    a = request.get_json()
    lis = pd.read_csv(r'db.csv')
    print(lis)
    #s = list(lis.to_dict('index').values())
    lis=lis[lis['index']!=a['index']]
    lis.to_csv('db.csv',index=None,header=True)
    #lsd=pd.read_csv(r'c:\Users\ADMIN\Desktop\data.csv')
    return jsonify(a['index'])

#if __name__== '__main__':
  #  app.run(debug=True,port=5000)
