# -*- encoding: utf-8 -*-
# Author: Administrator
# Date: 2022/10/15 18:37
# Describe:
from flask import render_template, request, Blueprint

cus = Blueprint("cus", __name__)


# 通过python装饰器的方法定义路由地址
@cus.route("/")
# 定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def root():
    return render_template("index.html")


# app的路由地址"/submit"即为ajax中定义的url地址，采用POST、GET方法均可提交
@cus.route("/submit", methods=["GET", "POST"])
# 从这里定义具体的函数 返回值均为json格式
def submit():
    # 由于POST、GET获取数据的方式不同，需要使用if语句进行判断
    global name, age
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
    if request.method == "GET":
        name = request.args.get("name")
        age = request.args.get("age")
    # 如果获取的数据为空
    if len(name) == 0 or len(age) ==0:
        return {'message': "error!"}
    else:
        return {'message': "success!", 'name': name, 'age': age}

