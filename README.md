# mysite

# pydjango

进入文件夹  
$ cd oa 

创建虚拟环境
$ python -m venv venv

激活虚拟环境  
$ source venv/bin/activate　　

安装Django
$ pip install django

创建项目为mysite （注意后面的点，代表当前路径下创建项目）
$ django-admin startproject mysite .

启动服务器运行项目  
(venv)$ python manage.py runserver　　
        python manage.py runserver 8080 (更改端口号)

创建应用 名字为clockin
(venv)$ python manage.py startapp clockin

退出虚拟环境  
(venv)$ deactive　　

 


pip install pylint-django　：vocode编程验证  
并添加配置 
"python.linting.pylintArgs": [
    "--load-plugins=pylint_django",
]

pip install bpmappers　：简化对象转成字典的操作   返回中文乱码 https://www.cnblogs.com/wf-skylark/p/9317096.html    json_dumps_params={'ensure_ascii':False})
pip install django-cors-headers　：　跨域　https://www.cnblogs.com/randomlee/p/9752705.html
pip install pymysql : 连接MySQL


mysql :  
    sudo -i 
    mysql  
    create database clockin default charset utf8;  
    grant all privileges on clockin.* to office@localhost identified by 'qwer1234';  

迁移：根据模型自动生成关系数据库中的二维表　　
python manage.py migrate　（迁移默认Django自带的数据模型）  

python manage.py makemigrations clockin　生成模型的迁移文件  
python manage.py migrate 迁移  



python manage.py createsuperuser : 创建管理员用户


INSERT INTO defaulttype  (name)  VALUES  ('其他'),('阅读写作'),('教育教养'),('学习考试');





Django那么多view，都写在同一个文件里面吗？

分不了的话views不一定是views.py, 也可以是
views/__init__.py 
"""
from .a import *
from .b import *
"""
views/a.py
views/b.py


增
models.UserInfo.objects.create(user='yangmv',pwd='123456')
或者
obj = models.UserInfo(user='yangmv',pwd='123456')
obj.save()
或者
dic = {'user':'yangmv','pwd':'123456'}
models.UserInfo.objects.create(**dic)

查
models.UserInfo.objects.all()
models.UserInfo.objects.all().values('user')    #只取user列
models.UserInfo.objects.all().values_list('id','user')    #取出id和user列，并生成一个列表
models.UserInfo.objects.get(id=1)
models.UserInfo.objects.get(user='yangmv')