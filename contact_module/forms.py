from django import forms
from contact_module.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        # exclude = ['email']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی',
                'id': 'full_name'
            }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',
                'id': 'email'
            }
            ),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان',
                'id': 'title'
            }
            ),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message',
                'placeholder': 'متن پیام'
            }
            ),
        }
        labels = {
            'message': 'متن پیام'
        }
