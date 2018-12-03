# import flask
from flask import Flask, render_template

#print(__name__)
app = Flask(__name__)     #生成应用实例
# app.config['DEBUG']=True
# 路由router
@app.route('/')       # 匹配请求地址
def index():
    name = '小明'
    age = 13
    return render_template('index.html',name=name,age=age)


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=8001)


"""
运行：
1.（CMD) python app.py
2.pycharm右键运行

修改代码：
编辑器代码修改后，由于内容中的代码还是原来的，需要重启服务，然后刷新浏览器。


这节课代码的几个阶段：
1.最简单return''
2.return'<h1>hello</h1>
3.前端代码放到专门的文件夹下。好处良好的分层。
4.自定义ip地址和端口
5.开启debug模式


app.run()方法，有几个参数
- host 并不是服务器的运行地址，服务器运行在本地，而是控制允许访问的客户端的地址段。默认127.0.0.1只允许自己浏览器访问，不允许局域网其他人访问。如果配置成'0.0.0.0'，表示接受任何ip地址的客户端，包括局域网其他人访问。

- port 端口，整数。
- （了解）threaded=True  开启多线程，局域网内接收多用户访问，实测也不够稳定
- debug=True,开启debug模式，修改代码服务器自动重启。也可以app.config['DEBUG']=True。看到日志Debug mode: on，为成功。目前是1.0.2版本。之前有一个版本刚才的设置并不会生效，原因是flask app运行时读取的是环境变量里的配置值，解决set  FLASK_DEBUG=True。
flask1.0.2版本，开启debug模式：
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
优点：敏感变量存入系统环境变量，flask命令启动时会去环境变量中读配置。flask命令除了包含python命令的解释功能，还增加与flask框架相关的功能。
pycharm中flask server

应用、wsgi通用网关接口、开发服务器：
应用：我们具体编写的业务逻辑代码。  比方说是  小米空气净化器
wsgi：                             比方  电源线电源插销
开发服务器：好像安卓应用需要运行在安卓系统上。类似java里的tomcat。    比方   220v电源
flask自带一个简单的开发服务器用来调式代码，但性能很弱，默认单进程单线程只能服务一个用户，人多之后服务无法响应。所以不能在生产服务器上直接运行flask自带的服务器

render_template()方法：
渲染模板。现获取html模板信息，插入后端变量，最终才返回给浏览器。
   # return’
   #         <html>
    #           <body>
    #                <h1>hello{}
    #           </body>
    #      </html>
    # '.format(name)
"""


"""
可能出现的错误：
1.not found 检查路由规则浏览器请求的url是否匹配
2.unicode decode error:postion 0 。flask 1.0.1源代码gethostaddr方法，如果windows主机名是中文就会报错。
3.修改代码，重启服务，刷新浏览器后结果没有改变。原因ctrl+c后并没有真正结束之前的服务，cmd中运行相关命令可以看到5000端口运行了多个服务。这样请求就到了之前的代码上。解决方法结束掉端口上的进程或重启
4.app.py 同级目录下新建了index.html,app.py文件中return render_template('index.html')，结果404。原因flask是一个完整的框架，有自己的规定，render_template函数会补全域名和template目录，所以这个函数的参数并不是一个普通的相对路径
5.修改代码没有生效。原因是pycharm启动了多个程序实例。解决方案应该只启动一个实例，代码修改后重启。
"""