from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizzas, name='pizzas'),
    path('pizza/<str:pk>', views.pizza, name='pizza'),
    path('add-pizza/', views.addPizza, name="add-pizza" ),
    path('update-pizza/<str:pk>', views.updatePizza, name="update-pizza"),
    path('delete-pizza/<str:pk>', views.deletePizza, name="delete-pizza"),
    path('delete-comment/<str:pk>', views.deleteComment, name="delete-comment"),
    path('update-comment/<str:pk>', views.updateComment, name="update-comment"),
]