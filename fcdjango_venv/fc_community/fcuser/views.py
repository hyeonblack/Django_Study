from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

# Create your views here.
def home(request):
    user_id = request.session.get('user', None)

    return render(request, 'home.html')

def login(request):
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)        
    #     password = request.POST.get('password', None)
    #     res_data = {}

    #     if not(username and password) :
    #         res_data['error'] = '모든 값을 입력해야합니다.'
    #     else:
    #         fcuser = Fcuser.objects.get(username=username)
    #         if check_password(password, fcuser.password):
    #             # 비밀번호 일치
    #             # 세션 설정
    #             # 리다이렉트
    #             request.session['user'] = fcuser.id
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '로그인 실패 하였습니다.'

    #     return render(request, 'login.html', res_data) 
    #    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()    
    return render(request, 'login.html', {'form':form})
        
def logout(request):
    if request.session.get('user'):
        del request.session['user']
    return redirect('/')

def regitser(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        
        res_data = {}

        if not(username and password and re_password and useremail):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!!!'
        else:            
            fcuser = Fcuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )            
            fcuser.save()


        return render(request,'register.html', res_data)