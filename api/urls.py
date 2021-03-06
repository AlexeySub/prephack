from django.urls import path, include
from api import views


urlpatterns = [
    path('users/', views.UserRegister.as_view()),
    path('auth/', views.UserAuth.as_view()),
    path('logout/', views.UserLogout.as_view()),
    path('chat/', views.Chat.as_view()),
    path('', views.index, name='index')
]
