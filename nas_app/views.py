# ./nas_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "로그인에 성공했습니다.")
            return redirect('dashboard')
        else:
            messages.error(request, "로그인 실패! 사용자 이름과 비밀번호를 확인해주세요.")
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    context = {
        'username': request.user.username,
        # 여기에 대시보드에 표시할 다른 데이터를 추가할 수 있습니다.
    }
    return render(request, 'dashboard.html', context)