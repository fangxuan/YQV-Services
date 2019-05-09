from flask import Blueprint, request

from api import db
from api.models.call_data_config_source import DataSource
from api.schemas.base import paginate_schema
from api.schemas.data_config import data_source_schema
from api.views.base import common_response, SysStatus, robot_response

blue_print = Blueprint('robot', __name__, url_prefix='/api/config')


@blue_print.route('/operatedatasource', methods=['POST'])
def data_source():
    params = data_source_schema(request.json or '')
    ismodify = params.get('ismodify')
    datasourceid = params.get('datasourceid')
    datasourcename = params.get('datasourcename')

    if ismodify:
        DataSource.query.filter(DataSource.id == datasourceid).update(name=datasourcename)
        db.session.commit()
    else:
        ds = DataSource()
        ds.name = datasourcename
        ds.save()
    return robot_response(SysStatus.SUCCESS, None, None)


@blue_print.route('/deletedatasource', methods=['POST'])
def data_source_delete():
    params = request.json
    datasourceid = params.get('datasourceid')

    if datasourceid:
        DataSource.query.filter(DataSource.id == datasourceid).delete()
        db.session.commit()
    else:
        return robot_response(SysStatus.FAIL, {"state": False}, None)
    return robot_response(SysStatus.SUCCESS, None, None)


@blue_print.route('/getgenretaglist', methods=['GET'])
def call_history():
    params = request.args
    page_index, page_size = paginate_schema(params)
    return robot_response(SysStatus.SUCCESS, (page_index, page_size), None)
