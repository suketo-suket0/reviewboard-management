# accounts/views.py
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)  # Djangoのログアウト処理を実行
    return redirect('login')  # ログアウト後にリダイレクトするURLを指定