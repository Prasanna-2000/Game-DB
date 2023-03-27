from django.shortcuts import render, redirect
from .models import Detail, Game, Info, Rating, Requirement
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    auth.logout(request)
    return render(request, "index.html")


def signup(request):

    if request.method == 'POST' :
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password==confirm_password :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                print('Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                print('Email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')

        else :
            print('password is not matching')
            messages.info(request, 'Password is not matching')
            return redirect('signup')
        return redirect('login')

    else:
        return render(request, "signup.html")


def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('gamepage')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, "login.html")

@login_required
def gamepage(request):
    games = Game.objects.all()
    return render(request, "game_page.html", {'games' : games})

@login_required
def mainpage(request, game_id):
    info = Info.objects.get(game_id = game_id)
    mgame = Game.objects.get(id = game_id)

    requirement = Requirement.objects.get(game_id = game_id)
    detail = Detail.objects.get(game_id = game_id)
    rating = Rating.objects.get(game_id = game_id)

    context = {'info' : info, 'game' : mgame,  'requirement' : requirement, 'detail' : detail, 'rating' : rating}
    return render(request, "mainpage.html", context)

def logout(request):
    auth.logout(request)
    return redirect('/')
