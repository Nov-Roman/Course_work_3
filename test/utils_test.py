import pytest
import utils


class TestPostDao:
    @pytest.fixture
    def posts_dao(self):
        return utils.PostsDao('data/data.json')

    @pytest.fixture
    def keys(self):
        return {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

    def test_check_type(self, posts_dao):
        """
        Проверка, посты должны быть списком, пост должен быть словарем
        """
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, 'Должен быть список'
        assert type(posts[0]) == dict, 'Должен быть словарь'

    def test_get_posts_all(self, posts_dao, keys):
        """
        Проверка соответствия ключей
        """
        posts = posts_dao.get_posts_all()
        first_post = posts[0]
        first_post_keys = set(first_post.keys())
        assert first_post_keys == keys, 'Ключи неверны'

    def test_one_check_type(self, posts_dao):
        """
        Проверка пост должен быть словарем
        """
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict, 'Должен быть словарь'

    def test_one_keys(self, posts_dao, keys):
        """
        Проверка соответствия ключей
        """
        post = posts_dao.get_post_by_pk(1)
        post_keys = set(post.keys())
        assert post_keys == keys, 'Ключи неверны'

    parameters_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    @pytest.mark.parametrize('post_pk', parameters_by_pk)
    def test_one_check_type_correct_pk(self, posts_dao, post_pk):
        """
        Проверка соответствия номера поста
        """
        post = posts_dao.get_post_by_pk(post_pk)
        assert post['pk'] == post_pk, "Неверный номер поста"

    def test_search_check_type(self, posts_dao):
        """
        Проверка пост должен быть списком
        """
        posts = posts_dao.search_for_posts('а')
        assert type(posts) == list, 'Должен быть список'

    def test_search_keys(self, posts_dao, keys):
        """
        Проверка соответствия ключей
        """
        post = posts_dao.search_for_posts('а')[0]
        post_keys = set(post.keys())
        assert post_keys == keys, 'Ключи неверны'

    questions_and_answers = [
        ('еда', [1]), ('дом', [2, 7, 8]), ('а', [1, 2, 3, 4, 5, 6, 7, 8])
    ]

    @pytest.mark.parametrize('questions, posts_pks', questions_and_answers)
    def test_search_right_match(self, posts_dao, questions, posts_pks):
        """
        Проверка соответствия данных
        """
        posts = posts_dao.search_for_posts(questions)
        pks = []
        for post in posts:
            pks.append(post['pk'])
        assert pks == posts_pks, 'Неверный поиск'

    def test_by_user_check_type(self, posts_dao):
        """
        Проверка, посты должны быть списком, пост должен быть словарем
        """
        posts = posts_dao.get_posts_by_user('leo')
        assert type(posts) == list, 'Должен быть список'
        assert type(posts[0]) == dict, 'Должен быть словарь'

    parameters_by_user = [
        ('leo', [1, 5]),
        ('hank', [3, 7]),
        ('johnny', [2, 6]),
    ]

    @pytest.mark.parametrize('user_name, posts_pks', parameters_by_user)
    def test_get_correct_user(self, posts_dao, user_name, posts_pks):
        posts = posts_dao.get_posts_by_user(user_name)
        pks = []
        for post in posts:
            pks.append(post['pk'])
        assert pks == posts_pks, 'Неверный поиск'
