from django import forms
from contact_module.models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        # required=False,
        error_messages={
            'required': 'لطفا نام و نام خانوادگی خود را وارد کنید'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        }
        )
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }
        )
    )
    title = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'عنوان'
        }
        )
    )
    message = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'متن پیام',
            'rows': '5',
            'id': 'message'
        }
        )
    )


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        # exclude = ['email']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }
            ),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
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