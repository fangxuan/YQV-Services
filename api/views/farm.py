from flask import Blueprint, request

from api import db
from api.models.farm import Plant, UserPlant
from api.schemas.base import paginate_schema
from api.serializer.farm import plant_basic_ser, user_plant_basic_ser
from api.views.base import common_response, SysStatus

blue_print = Blueprint('plants', __name__, url_prefix='/api/v0/plants')


@blue_print.route('/all', methods=['GET'])
def query_all_plants():
    """
       @api {GET} /api/v0/plants/all 获取所有植物
       @apiName get_wechat_payinfo
       @apiGroup wechatpay
       @apiSuccess {number} sys_status 状态码
       @apiSuccess {string} message  返回的信息
       @apiSuccess {dict} data 返回的数据
       @apiSuccess {string} appId 小程序ID
       @apiSuccess {string} timeStamp 时间戳
       @apiSuccess {string} nonceStr 随机串
       @apiSuccess {string} signType 签名方式
       @apiSuccess {string} package 数据包
       @apiSuccess {bool} paid 是否已支付，True 是， False 否
       @apiSuccessExample Success-Response:
      {"sys_status": "SUCCESS", "data": {"appId": "wx2993c8765d5647a9", "timeStamp": "1536301397", "nonceStr": "9azOH5IFQP1Yd7yVAqXMtgUirNLwElSs", "signType": "MD5", "package": "prepay_id=wx20180907142317490531", "paySign": "6D57EA634634A84DC352472576D47586", "paid":false}, "message": "\u6210\u529f"}
       @apiErrorExample Error-Response:
        {"data": null,"message": "失败","sys_status": 1}

    """
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
       @api {GET} /api/v0/plants/user 获取用户植物信息
       @apiName get_wechat_payinfo
       @apiGroup wechatpay
       @apiSuccess {number} sys_status 状态码
       @apiSuccess {string} message  返回的信息
       @apiSuccess {dict} data 返回的数据
       @apiSuccess {int} plant_id 植物ID
       @apiSuccess {bool} active_flag 是否激活
       @apiSuccess {int} water 水
       @apiSuccess {int} fertilizer 肥料
       @apiSuccess {int} pesticide 药物
       @apiSuccess {string} price 价格
       @apiSuccess {string} harvest_at 预计收获时间
       @apiSuccess {dict} status 状态
       @apiSuccess {string} image 预览图
       @apiSuccess {string} created_at 创建时间
       @apiSuccess {string} name 名称
       @apiSuccess {string} category 分类
       @apiSuccessExample Success-Response:
      {"sys_status": "SUCCESS", "data": {"pages": 1, "items": [{"plant_id": 1, "active_flag": true, "water": 80, "fertilizer": 54, "pesticide": 0, "price": "1.02", "harvest_at": "2019-05-31", "status": {"HEALTHY": "健康"}, "image": "http://image.antns.com/uploads/20171220/12/1513742641-BghOtrbPHu.jpg", "created_at": "2019-05-14 10:27:51", "name": "白菜", "category": "蔬菜"}, {"plant_id": 2, "active_flag": true, "water": 50, "fertilizer": 4, "pesticide": 0, "price": "2.00", "harvest_at": "2019-06-14", "status": {"HEALTHY": "健康"}, "image": null, "created_at": "2019-05-14 15:50:44", "name": "萝卜", "category": "蔬菜"}]}, "message": "成功"}
       @apiErrorExample Error-Response:
        {"data": null,"message": "失败","sys_status": 1}

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



