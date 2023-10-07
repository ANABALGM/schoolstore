from . import views
from django.urls import path

app_name='schoolapp1'

urlpatterns = [

    path('user_form/', views.user_form, name='user_form'),
    path('success/', views.success, name='success'),

]