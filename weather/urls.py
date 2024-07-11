from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cities/', views.add_city, name='cities'),
    path('weather/', views.weather, name='weather'),
    path('check/', views.create_weather, name='check'),
#     path('about/', views.about, name='about'),
    # path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    # path('password-reset', views.password_reset_request, name='password-reset'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='weather/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='weather/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='weather/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='weather/password_reset_complete.html'),
         name='password_reset_complete'),
     path('activate/<uidb64>/<token>', views.activate, name='activate')





]
