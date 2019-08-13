
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from voluptuous import MultipleInvalid
from api import create_app, DevConfig, db
from api.views.base import common_response, SysStatus


app = create_app(DevConfig)
# db = SQLAlchemy(app)
manager = Manager(app)


@app.errorhandler(MultipleInvalid)
def handle_exception(error):
    return common_response(SysStatus.PARAMETER_CHECK_ERROR, None, str(error))


Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
