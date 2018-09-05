#coding:utf-8

# 调用蓝图
from . import home
from flask import render_template,redirect, url_for


@home.route("/login/")
def login():
    return render_template("home/login.html")

@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))


@home.route("/regist/")
def regist():
    return render_template("home/regist.html")

@home.route("/user/") # 会员页面
def user():
    return render_template("home/user.html")

@home.route("/pwd/")   # 修改密码界面
def pwd():
    return render_template("home/pwd.html")

@home.route("/comments/")  # 评论界面
def comments():
    return render_template("home/comments.html")

@home.route("/loginlog/")  # 登录日志
def loginlog():
    return render_template("home/loginlog.html")

@home.route("/moviecol/")  # 电影收藏界面
def moviecol():
    return render_template("home/moviecol.html")

@home.route("/")
def index():
    return render_template("home/index.html")

@home.route("/animation/")
def animation():
    return render_template("home/animation.html")

@home.route("/search/")
def search():
    return render_template("home/search.html")

@home.route("/play/")
def play():
    return render_template("home/play.html")

