from app import create_app, db
from flask.ext.script import Manager, Shell, Server
from app.models import User


app = create_app('default') #create runing app from the factory
manager = Manager(app)      #use flask-script to manage app running

def make_shell_context():   #register shell command
    return dict(app = app, db = db, User = User)
manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command("debug", Server(host='0.0.0.0', port=8080))

if __name__ == '__main__':
    manager.run()