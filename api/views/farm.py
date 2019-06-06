from flask import Blueprint, request

from api import db
from api.models.farm import Plant, UserPlant
from api.schemas.base import paginate_schema
from api.serializer.farm import plant_basic_ser, user_plant_basic_ser
from api.views.base import common_response, SysStatus

blue_print = Blueprint('plants', __name__, url_prefix='/api/plants')


@blue_print.route('/all', methods=['GET'])
def query_all_plants():
    params = request.args
    page_index, page_size = paginate_schema(params)
    plants = Plant.query.with_entities(*plant_basic_ser).order_by(Plant.id).paginate(page=page_index,
                                                                                     per_page=page_size)
    data = {'pages': plants.pages, 'items': plants.items}
    return common_response(SysStatus.SUCCESS, data, None)


@blue_print.route('/user', methods=['GET'])
# @login_required(user_id)
def query_user_plants():
    """
    get water used and left
    :return:
    """
    params = request.args
    page_index, page_size = paginate_schema(params)
    user_plants = UserPlant.query.join(Plant).filter(UserPlant.user_id == 1).with_entities(*user_plant_basic_ser).order_by(
        UserPlant.id).paginate(page=page_index,
                               per_page=page_size)
    data = {'pages': user_plants.pages, 'items': user_plants.items}
    return common_response(SysStatus.SUCCESS, data, None)

# @blue_print.route('nurse', methods=['POST'])
# def nurse_plants():
#     """
#     get water/fertilizer user and total
#     :return:
#     """
#
#     params = request.args
#     id = params.get('id')
#     if id :
#         Ferti.query.fillter_by(Ferti.user_id = id)



