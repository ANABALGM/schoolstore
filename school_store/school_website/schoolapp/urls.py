from . import views
from django.urls import path, include

app_name='schoolapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('detail',views.detail,name='detail')
]