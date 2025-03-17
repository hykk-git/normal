from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, PostForm
from .models import Post

def main_view(request):
    return render(request, 'main.html')

def board_view(request):
    if not request.user.is_authenticated:
        return redirect('/signup/')  # 로그인하지 않은 사용자는 회원가입 페이지로 리디렉트
    return render(request, 'board.html')  # 로그인한 경우 게시판 표시

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # 비밀번호 암호화
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('board')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


@login_required
def board_view(request):
    posts = Post.objects.all()
    return render(request, 'board.html', {'posts': posts})

def post_list(request):
    return render(request, "post_list.html")