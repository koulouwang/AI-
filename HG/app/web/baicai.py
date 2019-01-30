# -*- coding:utf-8 -*-
# author : mt time:{2019/1/30}
from flask import Blueprint,render_template

baicai = Blueprint('baicai',__name__)

@baicai.route('/')
def index():

    return render_template('index.html')