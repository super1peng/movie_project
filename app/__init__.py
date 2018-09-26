#coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template
import os
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123lxp@127.0.0.1:3306/movie?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "4ae74f782f024748b71d33135d44a87a"
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")

app.debug = True
db = SQLAlchemy(app)

# 注册蓝图
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")   # 将后台加了一个"前缀"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404