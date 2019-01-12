# -*- coding:utf-8 -*-
# author : mt time:{2019/1/11}
from flask import Flask, make_response, jsonify
from yushubool import Yushubook
from helper import is_isbn_or_key

app = Flask(__name__)

@app.route('/book/search/<q>/<page>')
def hello(q,page):
    '''
    :param q: 视图函数
    :param page: 
    :return: 
    '''
    key_or_isbn = is_isbn_or_key(q)
    if key_or_isbn == 'isbn':
        result = Yushubook.search_by_isbn(q)
    else:
        result = Yushubook.search_by_keyword()
    return jsonify(result)
@app.route('/')
def index():
    return 'hello world'
app.run(debug=True,host='0.0.0.0')