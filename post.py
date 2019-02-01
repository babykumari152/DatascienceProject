from flask import Flask
from flask import jsonify
from flask import request,Blueprint
import pandas as pd
#app = Flask(__name__)

posts=Blueprint('posts',__name__)
@posts.route('/post',methods=["POST"])
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
#if __name__ == '__main__':
   # app.run(debug=True, port=5000)
