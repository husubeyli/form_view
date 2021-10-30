from django.urls import path

from accounts.views import RegisterView, profile, login, set_language

app_name = 'accounts'



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login, name='login'),
    path('profile/<int:id>/', profile, name='profile'),
    path('set_language/<str:lang_code>/', set_language, name="set_lang"),
]
