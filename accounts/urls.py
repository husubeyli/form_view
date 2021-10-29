from django.urls import path

from accounts.views import RegisterView, profile, login

app_name = 'accounts'



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login, name='login'),
    path('profile/<int:id>/', profile, name='profile'),
]
