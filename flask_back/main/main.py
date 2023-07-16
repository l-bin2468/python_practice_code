# -*- encoding: utf-8 -*-
# Author: Administrator
# Date: 2022/10/26 22:20
# Describe:
# 创建Flask对象app并初始化
from flask import Flask

from flask_route.action_route.action_flask import cus
from flask_route.admin.admin import admin
from flask_route.user.user import user

server = Flask(__name__, template_folder="../templates")
server.register_blueprint(cus, url_prefix="/cus")
server.register_blueprint(admin, url_prefix="/admin")
server.register_blueprint(user, url_prefix="/user")


if __name__ == '__main__':
    # print(server.url_map)
    # 定义app在8080端口运行
    server.run(host="0.0.0.0", port=8080, debug=True)
