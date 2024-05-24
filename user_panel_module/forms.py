from django import forms
from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'about_user', 'address']
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
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'درباره'
            }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'آدرس'
            }
            ),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'تصویر پروفایل',
            'address': 'آدرس',
            'about_user': 'درباره شخص'
        }
