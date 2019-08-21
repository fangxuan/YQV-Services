from flask import Blueprint

from api.views.base import SysStatus, common_response

blue_print = Blueprint('index', __name__, url_prefix='/api/v0/index')


@blue_print.route('/pictures', methods=['GET'])
def query_pictures():
    """
       @api {GET} /api/v0/index/pictures 首页轮播图
       @apiName query_pictures
       @apiGroup index
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
    demo_data = [
        {
            "id": 1,
            "name": "meinv10",
            "img_num": 10,
            "img_src": "https://picsum.photos/id/521/414/165"
        },
        {
            "id": 2,
            "name": "meinv05",
            "img_num": 10,
            "img_src": "https://picsum.photos/id/431/414/165"
        },
        {
            "id": 3,
            "name": "fengjing04",
            "img_num": 10,
            "img_src": "https://picsum.photos/id/65/414/165"
        },
        {
            "id": 4,
            "name": "fengjing05",
            "img_num": 11,
            "img_src": "https://images.unsplash.com/photo-1551334787-21e6bd3ab135?w=414"
        }
    ]

    return common_response(SysStatus.SUCCESS, demo_data, None)
