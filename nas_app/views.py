# ./nas_app/views.py

# ./nas_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"User {user.username} logged in successfully.")
            return redirect('dashboard')  # 로그인 성공 후 대시보드로 리디렉션
        else:
            print("Authentication failed.")
            # 로그인 실패 시 오류 메시지와 함께 로그인 페이지를 다시 렌더링
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 올바르지 않습니다.'})
    return render(request, 'login.html')


@login_required(login_url='/')
def dashboard_view(request):
    # 대시보드에 필요한 데이터를 추가할 수 있습니다.
    return render(request, 'dashboard.html')
