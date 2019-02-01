from flask import Flask
from flask import Blueprint, render_template
from get import gets
from post import posts
from delete import deletes
from put import puts

app = Flask('__name__')
#@app.route('/hello')
app.register_blueprint(gets)
app.register_blueprint(puts)
app.register_blueprint(posts)
app.register_blueprint(deletes)
@app.route('/')
def hello():
    return "Hello"
if __name__=='__main__':
    app.run(debug=True,port=5556)