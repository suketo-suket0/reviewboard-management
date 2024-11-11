from django.urls import path
from accounts.views import logout
from django.contrib import admin

app_name = "accounts"

urlpatterns =[
    path('admin/', admin.site.urls),
    path('login/', name = 'login'),
    path('', logout, name = 'logout'),
]