# ./nas_project/urls.py

from django.contrib import admin
from django.urls import path
from nas_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # 파일 관리 기능 관련 URL 패턴
    # path('upload/', views.file_upload_view, name='file_upload'),  # 이 줄을 주석 처리 또는 제거
    path('files/', views.file_list_view, name='file_list'),
    path('download/<int:file_id>/', views.file_download_view, name='file_download'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)