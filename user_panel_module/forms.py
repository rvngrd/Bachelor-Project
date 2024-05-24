from django import forms
from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام'
            }
            ),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی'
            }
            ),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'تصویر پروفایل'
            }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'id': 'message',
                'placeholder': 'آدرس'
            }
            ),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'تصویر پروفایل',
            'address': 'آدرس',
        }
