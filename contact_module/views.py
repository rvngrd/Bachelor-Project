from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, View
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs

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


class CreateProfileView(View):
    def get(self, request):
        return render(request, 'contact_module/create_profile_page.html')

    def post(self, request):
        print(request.FILES)
        return redirect('/contact-us/create-profile')
