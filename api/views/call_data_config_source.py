from flask import Blueprint, request

from api.extensions import db
from api.models.call_data_config_source import DataSource
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
    else:
        ds = DataSource()
        ds.name = datasourcename
        ds.save()
    return robot_response(SysStatus.SUCCESS, None, None)
