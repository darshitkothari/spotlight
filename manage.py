# Application Entry Point File

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db  # , admin

from app.main.controller.routes_ep.error_routes import error
from app.main.controller.routes_ep.auth_routes import auth
from app.main.controller.routes_ep.main_routes import main
from app.main.controller.routes_ep.admin_routes import admin
# from app.main.controller.routes_ep.admin_routes import Users, Policies

# from flask_admin.contrib.sqla import ModelView
# from app.main.models.user import User
# admin.add_view(ModelView(User, db.session))

app = create_app('dev')

# Registering Blueprints
app.register_blueprint(error)
app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(admin)

# admin.add_view(Users(name='Users', endpoint='users'))
# admin.add_view(Users(name='Policies', endpoint='policies'))

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(ssl_context="adhoc", threaded=True)


if __name__ == '__main__':
    manager.run()