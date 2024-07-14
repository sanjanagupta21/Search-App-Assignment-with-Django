
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('dish-search/', views.dish_search_view, name='dish_search'),
]
