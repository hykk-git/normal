from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, PostForm
from .models import Post

def main_view(request):
    return render(request, 'main.html')

def board_view(request):
    # is_authenticated로 로그인 여부 체크
    if not request.user.is_authenticated:
        # 로그인하지 않은 사용자는 회원가입 페이지로 리다이렉트
        return redirect('/signup/')  
    return render(request, 'board.html') 

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Django는 기본적으로 비밀번호 해시해서 저장
            user.set_password(form.cleaned_data['password']) 
            user.save()
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            # 로그인 이후 main으로 이동
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # 로그아웃 이후 main으로 이동
    return redirect('/')

@login_required
def board_view(request):
    posts = Post.objects.all()
    return render(request, 'board.html', {'posts': posts})