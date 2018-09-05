#coding:utf-8

# 蓝图的注册
from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views