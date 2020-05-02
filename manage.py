# Application Entry Point File

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db

from app.main.controller.routes_ep.error_routes import error
from app.main.controller.routes_ep.auth_routes import auth
from app.main.controller.routes_ep.main_routes import main

app = create_app('dev')

# Registering Blueprints
app.register_blueprint(error)
app.register_blueprint(auth)
app.register_blueprint(main)

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(ssl_context="adhoc", threaded=True)


if __name__ == '__main__':
    manager.run()