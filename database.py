from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import User

manager = Manager(app)
# 第一个参数是flask实例，第二个参数SQLAlchemy实例
Migrate(app, db)

# manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()


"""
实际操作顺序:
1.python database.py db init
2.python database.py db migrate -m"版本名(注释)"
3.python database.py db upgrade 然后观察表结构
4.根据需求修改模型
5.python database.py db migrate -m"新版本名(注释)"
6.python database.py db upgrade 然后观察表结构
7.若返回版本,则利用 python 文件 db history查看版本号
8.python database.py db downgrade(upgrade) 版本号
"""