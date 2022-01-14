import multiprocessing
workers = 2
bind = '127.0.0.1:8095'
#daemon = True
pidfile = '/run/gunicorn.pid'
timeout = 30
worker_class = 'gevent'
worker_connections = 200
keepalive = 2
daemon = False  # 启动后台进程（当supervisor管理进程时需要False)
chdir = '/opt/vulscan'
loglevel = 'debug'
accesslog = '/var/log/gunicorn/vulscan_access.log'
errorlog = '/var/log/gunicorn/vulscan__error.log'
