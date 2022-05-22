import json


class CommentsDao:

    def __init__(self, path):
        self.path = path

    def load_comments(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_comments_by_post_id(self, post_id):
        """
        Возвращает комментарии определенного поста
        """
        comments = self.load_comments()
        comments_by_id = []
        for comment in comments:
            if comment['post_id'] == post_id:
                comments_by_id.append(comment)
        return comments_by_id
