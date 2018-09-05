#coding:utf-8

# 调用蓝图
from . import admin

@admin.route("/")
def index():
    return "<h1 style= 'color:red'>this is admin</h1>"