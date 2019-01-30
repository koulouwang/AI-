# -*- coding:utf-8 -*-
# author : mt time:{2019/1/30}
from app import create_app

app = create_app()
@app.route('/')
def index():
    return 'hellow'


if __name__ == '__main__':
    app.run()