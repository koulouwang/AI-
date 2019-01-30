# -*- coding:utf-8 -*-
# author : mt time:{2019/1/30}

from flask import Flask

def register_bp(app):
    from app.web.baicai import baicai
    app.register_blueprint(baicai,url_prefix='/baicai')
def create_app():
    '''
    
    :return:创建的app对象 
    '''
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    register_bp(app)
    return app