from main import app


class TestApi:

    def test_all_status_code(self):
        """
        Проверка получения нужного формата
        """
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, 'Код запроса постов неверный'
        assert response.mimetype == 'application/json', 'Неверный формат'

    def test_one_post_status_code(self):
        """
        Проверка получения нужного формата
        """
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert response.status_code == 200, 'Код запроса поста неверный'
        assert response.mimetype == 'application/json', 'Неверный формат'

    def test_app_posts_type_check_keys(self):
        """
        Проверка, что у элементов есть нужные ключи
        """
        keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
        response = app.test_client().get('/api/posts', follow_redirects=True)
        first_keys = set(response.json[0].keys())
        assert keys == first_keys, 'Ключи неверны'

    def test_post_type_count_check(self):
        """
        Проверка получения списка
        """
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert type(response.json) == list, 'Получен не список'

    def test_one_post_type_count_check(self):
        """
        Проверка получения словаря
        """
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert type(response.json) == dict, 'Получен не словарь'







