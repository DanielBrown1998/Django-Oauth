from django.urls import path
from tech import views

app_name = 'tech'

urlpatterns = [
    path('', views.index, name='index'),
]

