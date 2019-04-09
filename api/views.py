from api.models import User, UserAuthen
from api.serializers import UserSerializer
from rest_framework import renderers, parsers, views, viewsets, generics
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.core import exceptions
from django import db


class UserRegister(View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        data['password'] = make_password(data['password'], salt='123')
        user = User(name=data['username'], password=data['password'], email=data['email'], userType=data['usertype'])
        try:
            user.save()
        except db.IntegrityError:
            return HttpResponse('Conflict', status=409)
        return HttpResponse('ee')


class UserAuth(View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        try:
            user = User.objects.get(name=data['login'])
        except exceptions.ObjectDoesNotExist:
            return HttpResponse('Unauthorized', status=401)
        if user.password == make_password(data['password'], salt='123'):
            userAuth = UserAuthen(user_id=user.id, token='ee4', is_authenticated=True)
            userAuth.save()
            return HttpResponse(renderers.JSONRenderer().render({'auth_token':'ee4'}))
        else:
            return HttpResponse('Unauthorized', status=401)


class UserLogout(View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        userAuth = UserAuthen.objects.get(token=data['auth_token'])
        userAuth.is_authenticated=False
        userAuth.save()
        return HttpResponse('Ok(')

