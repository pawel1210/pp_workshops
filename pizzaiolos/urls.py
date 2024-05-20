from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('account/', views.account, name='account'),
    path('', views.pizzaiolos, name='pizzaiolos'),
    path('profile/<str:pk>/', views.pizzaiolo, name='pizzaiolo'),
    path('edit-pizzaiolo/', views.editPizzaiolo, name='edit-pizzaiolo'),
    path('inbox/', views.inbox, name="inbox"),
    path('inbox/<str:pk>/', views.conversation, name="conversation"),

]