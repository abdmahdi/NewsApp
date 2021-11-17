from django.urls import path
from News import views


urlpatterns = [
    path('', views.index, name='index')
]
