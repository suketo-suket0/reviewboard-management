from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db import connection

class MySQLBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # MySQLのクエリを使ってユーザーデータを取得
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, username, password FROM user_table WHERE username = %s", [username])
            row = cursor.fetchone()

            if row and self.check_password(password, row[2]):
                try:
                    user = User.objects.get(username=row[1])
                except User.DoesNotExist:
                    # ユーザーが存在しない場合、新規作成
                    user = User(username=row[1])
                    user.set_password(row[2])
                    user.save()
                return user
        return None

    def check_password(self, raw_password, hashed_password):
        # パスワードのハッシュを検証する
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, hashed_password)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None