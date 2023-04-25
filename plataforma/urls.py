from django.urls import path

from . import views

app_name = 'plataforma'

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('produto/', views.produto, name='produto'),

]
