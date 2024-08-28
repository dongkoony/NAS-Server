# ./nas_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.conf import settings
import os
from .models import NASFile
from .forms import FileUploadForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 올바르지 않습니다.'})
    return render(request, 'login.html')

@login_required(login_url='/')
def dashboard_view(request):
    if request.method == 'POST':
        print(request.FILES)
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nas_file = form.save()
            print(f"File saved at: {nas_file.file.path}")  # 저장된 파일의 경로를 출력
            print(f"MEDIA_ROOT is set to: {settings.MEDIA_ROOT}")
            return redirect('dashboard')
        else:
            print("Form is not valid.")
            print(form.errors)  # 폼 오류를 출력하여 문제를 진단
    else:
        form = FileUploadForm()
    
    files = NASFile.objects.all()
    return render(request, 'dashboard.html', {'form': form, 'files': files})

@login_required(login_url='/')
def file_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'file_upload.html', {'form': form})

@login_required(login_url='/')
def file_list_view(request):
    files = NASFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

@login_required(login_url='/')
def file_download_view(request, file_id):
    try:
        nas_file = NASFile.objects.get(id=file_id)
        file_path = os.path.join(settings.MEDIA_ROOT, nas_file.file.name)
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    except NASFile.DoesNotExist:
        raise Http404("File does not exist")
