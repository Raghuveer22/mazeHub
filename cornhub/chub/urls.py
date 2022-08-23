from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='chub/login.html'), name='login'),
    path('home',views.home,name='home'),
    path('q2',views.q2,name='q2'),
    path('q3',views.q3,name='q3'),
    path('q4',views.q4,name='q4'),


]