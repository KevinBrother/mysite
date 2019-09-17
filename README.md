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

创建应用 名字为clockin
(venv)$ python manage.py startapp clockin

退出虚拟环境  
(venv)$ deactive　　

    python manage.py makemigrations vote
    python manage.py migrate


pip install pylint-django　：vocode编程验证  
pip install bpmappers　：简化对象转成字典的操作 返回中文乱码 https://www.cnblogs.com/wf-skylark/p/9317096.html  
pip install django-cors-headers　：　跨域　https://www.cnblogs.com/randomlee/p/9752705.html
