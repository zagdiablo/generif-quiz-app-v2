from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import forms

app_name = 'core'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name='public/login.html',
                                      authentication_form=forms.LoginForm),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard')
]
