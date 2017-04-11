# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
import json
app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify({'result':a + b,'code': -1,'msg': 'hello world','data':{'one':a,'two':b}})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
