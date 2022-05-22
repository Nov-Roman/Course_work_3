import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, abort, request

import utils
import comments_dao

posts_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')
posts_dao = utils.PostsDao('data/data.json')
comments_dao = comments_dao.CommentsDao('data/comments.json')
logger = logging.getLogger('basic')


@posts_blueprint.route('/')
def post_all():
    """
    Вывод всех постов
    """
    logger.debug('Запрошены все посты')

    try:
        posts = posts_dao.get_posts_all()
        return render_template('index.html', posts=posts)
    except BaseException as e:
        return render_template('error.html', error=e)


@posts_blueprint.route('/posts/<int:post_pk>')
def post_one(post_pk):
    """
    Вывод постов
    """
    logger.debug(f'Запрошены посты {post_pk}')

    try:
        post = posts_dao.get_post_by_pk(post_pk)
        comments = comments_dao.get_comments_by_post_id(post_pk)
    except (JSONDecodeError, FileNotFoundError) as error:
        return render_template('error.html', error=error)
    except BaseException as e:
        return render_template('error.html', error=e)

    else:
        if post is None:
            abort(404)
        count_comments = len(comments)
        return render_template('post.html', post=post, comments=comments, count_comments=count_comments)


@posts_blueprint.errorhandler(404)
def post_error():
    return 'Пост не найден', 404


@posts_blueprint.route('/search')
def post_search():
    """
    Вывод информации по запросу
    """
    query = request.args.get('s', '')

    if query != '':
        posts = posts_dao.search_for_posts(query)
        number_of_posts = len(posts)
    else:
        posts = []
        number_of_posts = 0

    return render_template('search.html', query=query, posts=posts, number_of_posts=number_of_posts)


@posts_blueprint.route('/users/<username>')
def post_user_search(username):
    """
    Вывод пользователя
    """
    posts = posts_dao.get_posts_by_user(username)
    number_of_posts = len(posts)
    return render_template('user-feed.html', username=username, posts=posts, number_of_posts=number_of_posts)
