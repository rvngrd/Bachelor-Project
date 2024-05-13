from django.shortcuts import render, redirect


# Create your views here.


def contact_us_page(request):
    if request.method == 'POST':
        print(request.POST['email'])
        return reversed(redirect('home_page'))
    return render(request, 'contact_module/contact_us_page.html')
