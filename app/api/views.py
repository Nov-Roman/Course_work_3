import logging
import utils
import comments_dao
from flask import Blueprint, jsonify

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')

posts_dao = utils.PostsDao('data/data.json')
comments_dao = comments_dao.CommentsDao('data/comments.json')
logger = logging.getLogger('basic')


@api_blueprint.route('/api/posts/')
def post_all():
    """
    Информация о запросе всех постов
    """
    logger.debug("Запрошены все посты (api)")
    posts = posts_dao.get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>/')
def post_one(post_id):
    """
    Информация о запросе поста
    """
    logger.debug(f"Запрошен пост {post_id} (api)")
    post = posts_dao.get_post_by_pk(post_id)
    return jsonify(post)
