from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.views.generic import TemplateView, FormView, RedirectView, DetailView


# Create your views here.
class UserLogin(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    
    # def form_valid(self, form):
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password']





