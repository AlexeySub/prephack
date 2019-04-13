from api.models import User, UserAuthen, Message
from rest_framework import renderers, parsers
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.core import exceptions
from django import db
import jwt, time
from django.shortcuts import render


class UserRegister(View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        data['password'] = make_password(data['password'], salt='123')
        user = User(name=data['username'].lower(), password=data['password'], email=data['email'].lower(), userType=data['usertype'])
        try:
            user.save()
        except db.IntegrityError:
            return HttpResponse('Conflict', status=409)
        return HttpResponse('OK', status=200)


class UserAuth(View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data['login'].lower())
        try:
            user = User.objects.get(name=data['login'].lower())
        except exceptions.ObjectDoesNotExist:
            return HttpResponse('Unauthorized', status=401)
        if user.password == make_password(data['password'], salt='123'):
            authtoken = jwt.encode(data, 'secret', algorithm='HS256').decode('UTF-8')
            userAuth = UserAuthen(user_id=user.id, token=authtoken, is_authenticated=True)
            userAuth.save()
            return HttpResponse(renderers.JSONRenderer().render({'auth_token': authtoken}))
        else:
            return HttpResponse('Unauthorized', status=401)


class UserLogout(View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        userAuth = UserAuthen.objects.get(token=data['auth_token'])
        userAuth.is_authenticated=False
        userAuth.save()
        return HttpResponse('Ok')


class Chat(View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        try:
            jwt.decode(data['auth_token'], 'secret', algorithm='HS256')
        except jwt.InvalidSignatureError:
            return HttpResponse('Unathorized', status=401)
        message = Message(user_id=UserAuthen.objects.get(token=data['auth_token']).user_id, text=data['text'])
        try:
            message.save()
        except db.IntegrityError:
            return HttpResponse('Conflict', status=409)
        return HttpResponse('OK', status=200)

    def get(self, request):
        data = parsers.JSONParser().parse(request)
        try:
            jwt.decode(data['auth_token'], 'secret', algorithm='HS256')
        except jwt.InvalidSignatureError:
            return HttpResponse('Unathorized', status=401)
        chat = Message.objects.all().filter(user_id=User.objects.get(name=data['login']).id)
        return HttpResponse(renderers.JSONRenderer().render(chat.text))


def index(request):
    return render(request, 'index.html')

