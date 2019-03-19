from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from voluptuous import MultipleInvalid
from api import create_app, DevConfig, db
from api.views import user, recommend
from api.views.base import common_response, SysStatus


def reg_blueprints(app):
    app.register_blueprint(user.blue_print)
    app.register_blueprint(recommend.blue_print)
    return None


app = create_app(DevConfig)
# db = SQLAlchemy(app)
manager = Manager(app)


@app.errorhandler(MultipleInvalid)
def handle_exception(error):
    return common_response(SysStatus.PARAMETER_CHECK_ERROR, None, str(error))


Migrate(app, db)
# cache.init_app(my_app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
