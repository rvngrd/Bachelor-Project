from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views import View
from account_module.forms import RegisterForm

# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # todo: register user
            pass
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)
