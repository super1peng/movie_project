# 电影项目
Flask 开发训练

项目文件介绍
微电影网站：  
* 前台模块（home）
* 后台模块（admin）

## 前台模块(home)
数据模型：models.py
表单处理：home/forms.py
模板目录：templates/home

## 后台模块(admin)
数据模型：models.py
表单处理：admin/forms.py  
模板目录：templates/admin
静态目录：static  

# 蓝图构建

什么是蓝图
一个应用中或者跨应用组件和支持用用的模式
蓝图的作用  

1. 将不同的功能模块化  
2. 构建大型应用  
3. 优化项目结构  
4. 增强可读性，易于维护


## 管理员登录
在forms.py中定义表单  
在html中使用表单字段、信息验证、消息闪现  
views中处理登录请求，保存会话  
views中定义登录装饰器、访问控制

1. 模型：Admin  
2. 表单：LoginForm  
3. 请求方法： GET POST  
4. 访问控制：无  