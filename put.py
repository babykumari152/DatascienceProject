from flask import Flask
from flask import jsonify
from flask import request,Blueprint
import pandas as pd
puts=Blueprint('puts',__name__)
#app = Flask(__name__)
@puts.route('/put',methods=["PUT"])
def put():
    a = request.get_json()
    lis = pd.read_csv('db.csv')
    s = list(lis.to_dict('index').values())
    lis[lis['index'] == a['index']]['name'] = a['name']
    lis[lis['index'] == a['index']]['class'] = a['class']
    lis[lis['index'] == a['index']]['rollno'] = a['rollno']
    lis.to_csv('db.csv',index=None,header=True)
    ls = list(lis.to_dict('index').values())
    print("Doing")
    return jsonify(ls)
#if __name__ == '__main__':
  #  app.run(debug=True, port=5000)
