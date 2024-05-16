from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, View, ListView
from .forms import ContactUsModelForm
from .models import UserProfile


# Create your views here.


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    #
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def post(self, request):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return render(request, 'contact_module/contact_us_page.html', context={
    #             'contact_form': contact_form
    #         })


def store_file(file):
    with open('temp/image.jpg', "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'


class ProfileViews(ListView):
    model = UserProfile
    template_name = 'contact_module/profiles_list_page.html'
    context_object_name = 'profiles'
