from django.shortcuts import redirect, render
from django.views import generic
from django.urls.base import reverse, reverse_lazy

from django.urls import translate_url
from django.utils import translation
from django.contrib.gis.geoip2 import GeoIP2


from django.contrib.messages import success
from accounts.models import Consumer


from .forms import RegisterForm, LoginForm
# Create your views here.

class RegisterView(generic.CreateView):
    model = Consumer
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('accounts:register')

    def form_invalid(self, form):
        print(form.errors, 'error')
        return super().form_invalid(form)


def login(request):
    template = 'login.html'
    form = LoginForm
    if request.method == 'POST':
        code = request.POST.get('secret_key')
        print(code, 'salam')
        user = Consumer.objects.filter(secret_key=code)
        user_id = Consumer.objects.filter(secret_key=code).first()
        if user.exists():
            success(request, 'Good')
            return redirect('accounts:profile', id=user_id.id)
        else:
            # messages.warning(request, "The username or password are not valid!")
            success(request, 'This is client id not registered')
            return redirect(reverse('accounts:login'))
    context = {'form': form}
    return render(request, 'login.html', context)


def profile(request, id):
    user = Consumer.objects.get(id=id)
    return render(request, 'profile.html', context={'user': user})


def set_language(request, lang_code):
    lang = request.META.get("HTTP_REFERER", None)
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        
    g = GeoIP2()
    location = g.city(ip)
    location_country = location["country_name"]
    location_city = location["city"]
    print(location_country, location_city, 'alsalam')
    response = redirect(translate_url(lang, lang_code))
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code

    return response