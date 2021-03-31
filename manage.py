# Application Entry Point File

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db  # , admin
from app.main.models import user, policy, department
from app import blueprint
from app.main.controller.routes_ep.error_routes import error
from app.main.controller.routes_ep.auth_routes import auth
from app.main.controller.routes_ep.main_routes import main
from app.main.controller.routes_ep.admin_routes import admin

app = create_app('dev')

# Registering Blueprints
app.register_blueprint(blueprint)
app.register_blueprint(error)
app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(admin)

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(ssl_context="adhoc", threaded=True)


if __name__ == '__main__':
    manager.run()
