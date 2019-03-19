from flask import Blueprint

# from api.models.recommend import Article
from api.views.base import common_response, SysStatus

blue_print = Blueprint('recommend', __name__, url_prefix='/api/recommend')


@blue_print.route('/article', methods=['GET'])
def article_recommend():
    # article = Article.query.filter(Article.id == 1).all().paginate(page=1, per_page=5)
    data = {'user_id': 1, 'name': 'Gemingyu'}
    return common_response(SysStatus.SUCCESS, data, None)
