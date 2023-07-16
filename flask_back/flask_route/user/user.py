# -*- encoding: utf-8 -*-
# Author: Administrator
# Date: 2022/10/26 22:36
# Describe:
from flask import Blueprint, render_template
user = Blueprint("user", __name__)


@user.route("/index")
def index():
    return render_template("index.html")


@user.route("/add")
def add():
    return "user_add"


@user.route("/show")
def show():
    return "user_show"
