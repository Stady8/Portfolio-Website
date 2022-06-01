from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('webapp', views.webApp, name='webapp'),
    path('mazegame', views.mazegame, name='mazegame'),
    path('vrgame', views.vrgame, name='vrgame'),
    path('trailer', views.trailer, name='trailer'),
    path('resume', views.resume, name='resume')
]