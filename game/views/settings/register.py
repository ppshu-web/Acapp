from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from game.models.player.player import Player



def register(request):
    data = request.GET
    username = data.get("username", "").strip(); #strip可以将前后的空格去掉
    password = data.get("password", "").strip();
    password_confirm = data.get("password_confirm", "").strip()
    if not username or not password:
        return JsonResponse({
            'result': "Username and password fields cannot be blank.",
        })
    if password != password_confirm:
        return JsonResponse({
            'result': "Passwords do not match.",
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': "Username exists",
        })
    user = User(username=username)
    user.set_password(password)
    user.save()
    Player.objects.create(user=user, photo="https://img0.baidu.com/it/u=2826258537,2867921226&fm=253&fmt=auto?w=800&h=800")
    login(request, user)
    return JsonResponse({
        'result': "success"
    })
