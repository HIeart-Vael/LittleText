from mytext import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('record', views.record, name='record'),
    path('search', views.search),
]
