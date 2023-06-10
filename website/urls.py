from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('page', views.page1, name='page'),
    path('page1', views.page2, name='page1'),
    path('page2', views.page3, name='page2'),
]