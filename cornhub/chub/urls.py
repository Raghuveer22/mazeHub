from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='chub/login.html'), name='login'),
    path('1',views.q1,name='1'),
    path('2',views.q2,name='2'),
    path('3',views.q3,name='3'),
    path('4',views.q4,name='4'),
    path('5',views.q5,name='5'),
]