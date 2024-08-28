# ./nas_project/urls.py

from django.contrib import admin
from django.urls import path
from nas_app import views
from django.conf import settings  # settings 파일에서 MEDIA_URL과 MEDIA_ROOT를 가져오기 위해 필요
from django.conf.urls.static import static  # 정적 파일 처리를 위한 모듈

urlpatterns = [
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('', views.login_view, name='login'),  # 첫 페이지를 로그인 페이지로 설정
    path('dashboard/', views.dashboard_view, name='dashboard'),  # 로그인 후 리디렉션될 대시보드 페이지
    
    # 파일 관리 기능 관련 URL 패턴
    path('upload/', views.file_upload_view, name='file_upload'),  # 파일 업로드 페이지
    path('files/', views.file_list_view, name='file_list'),  # 파일 목록 페이지
    path('download/<int:file_id>/', views.file_download_view, name='file_download'),  # 파일 다운로드 URL
]

# 개발 서버에서 MEDIA 파일을 서빙할 수 있도록 설정
# 실제 배포 환경에서는 웹 서버에서 이 설정을 처리해야 합니다.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
