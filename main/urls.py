from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.index, name="index"),
    path('home/', views.home, name="home"),
    path('', views.home, name="home"),
    path('create/',views.createList, name="create"),
    path('view/',views.view, name="view"),
]