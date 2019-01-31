from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd
app = Flask(__name__)


@app.route('/post',methods=["POST"])
def post():
    lis = pd.read_csv('db.csv')
    #s = list(lis.to_dict('index').values())
    a = request.get_json()
    new = {}
    new['index'] = lis.iloc[-1]['index'] + 1
    print(new)

    combineds = {**new,**a}
    print(combineds)
    lis = lis.append(combineds,ignore_index=True)
    lis.to_csv('db.csv',index=None,header=True)
    return jsonify(int(new['index']))

@app.route('/get', methods=["GET"])
def get():

    lis = pd.read_csv(r'C:\Users\ADMIN\Desktop\datacsv.csv')
            #print(lis)
    lm=lis.to_dict('index')
            #print(lm)
    print("abc")
    s = list(lis.to_dict('index').values())
    return jsonify(s)

@app.route('/put',methods=["PUT"])
def put():
    a = request.get_json()
    lis = pd.read_csv(r'C:\Users\ADMIN\Desktop\datacsv.csv')
    s = list(lis.to_dict('index').values())
    lis[lis['index'] == a['index']]['name'] = a['name']
    lis[lis['index'] == a['index']]['class'] = a['class']
    lis[lis['index'] == a['index']]['rollno'] = a['rollno']
    lis.to_csv('data.csv',index=None,header=True)
    ls = list(lis.to_dict('index').values())
    print("Doing")
    return jsonify(ls)

@app.route('/delete',methods=["DELETE"])
def dels():
    a = request.get_json()
    lis = pd.read_csv(r'C:\Users\ADMIN\Desktop\datacsv.csv')
    print(lis)
    #s = list(lis.to_dict('index').values())
    lis=lis[lis['index']!=a['index']]
    lis.to_csv(r'C:\Users\ADMIN\Desktop\datacsv.csv',index=None,header=True)
    #lsd=pd.read_csv(r'c:\Users\ADMIN\Desktop\data.csv')


    return jsonify(a['index'])

if __name__== '__main__':
    app.run(debug=True,port=5000)
