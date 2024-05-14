from django import forms


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
    subject = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'عنوان'
        }
        )
    )
    text = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'متن پیام',
            'rows': '5',
            'id': 'message'
        }
        )
    )
