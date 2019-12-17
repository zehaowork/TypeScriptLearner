from django.urls import path

from . import views

app_name = 'interpreter'
urlpatterns = [
    path('',views.index, name='index')
]