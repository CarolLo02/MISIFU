from django.urls import path
from .views import login_view, logout_view, ingreso_view, signup_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('ingreso/', ingreso_view, name='ingreso'),
    path('signup/', signup_view, name='signup'),
]
