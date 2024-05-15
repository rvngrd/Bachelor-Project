from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'home_module/index_page.html')


# class HomeView(TemplateView):
#     template_name = 'home_module/index_page.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = 'salam!'
#         return context


def site_header_component(request):
    return render(request, 'shared/site_header_component.html', {})


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html', {})
