# ./nas_project/urls.py

from django.contrib import admin
from django.urls import path
from nas_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # 첫 페이지를 로그인 페이지로 설정
    path('dashboard/', views.dashboard_view, name='dashboard'),  # 로그인 후 리디렉션될 페이지
]
