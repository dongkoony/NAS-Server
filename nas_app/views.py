# ./nas_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # 로그인 성공 후 대시보드로 리디렉션
        else:
            return HttpResponse("로그인 실패! 다시 시도하세요.")
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    return HttpResponse("대시보드에 오신 것을 환영합니다!")
