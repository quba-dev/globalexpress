from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('email/', views.forget_email, name='forget_email'),
    path('reset/<int:pk>/<str:token>/', views.reset, name='reset'),
]