# ./nas_app/views.py

import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.conf import settings
from django.contrib import messages

from .models import NASFile
from .forms import MultipleFileUploadForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '로그인에 성공했습니다.')
            return redirect('dashboard')
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
    return render(request, 'login.html')

@login_required(login_url='/')
def dashboard_view(request):
    if request.method == 'POST':
        form = MultipleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('files')
            description = form.cleaned_data['description']
            for file in files:
                NASFile.objects.create(file=file, description=description)
            messages.success(request, f'{len(files)}개의 파일이 성공적으로 업로드되었습니다.')
            return redirect('dashboard')
        else:
            messages.error(request, '파일 업로드 중 오류가 발생했습니다. 다시 시도해주세요.')
    else:
        form = MultipleFileUploadForm()
    
    files = NASFile.objects.all()
    return render(request, 'dashboard.html', {'form': form, 'files': files})

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