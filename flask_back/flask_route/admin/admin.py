# -*- encoding: utf-8 -*-
# Author: Administrator
# Date: 2022/10/26 22:36
# Describe:
from flask import Blueprint, render_template
admin = Blueprint("admin", __name__)


@admin.route("/index")
def index():
    return render_template("index.html")


@admin.route("/add")
def add():
    return "admin_add"


@admin.route("/show")
def show():
    return "admin_show"
