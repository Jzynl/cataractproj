from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('upload/', views.upload_view, name='upload'),
    path('result/<int:scan_id>/', views.result_view, name='result'),
    path('history/', views.history_view, name='history'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
