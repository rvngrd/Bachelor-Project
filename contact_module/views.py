from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import ContactUsForm, ContactUsModelForm


# Create your views here.


class ContactUsView(FormView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def post(self, request):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return render(request, 'contact_module/contact_us_page.html', context={
    #             'contact_form': contact_form
    #         })
