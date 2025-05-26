from django.urls import path
from user.views import RegisterView, login_user, logout_user
from home.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
