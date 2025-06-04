from django import forms
from django.core import validators



class ContactsForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'عنوان',
        'id' : 'title'
    }))

    f_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control text-left',
        'placeholder' : 'نام',
        'id' : 'name'
    }))

    l_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'نام خانوادگی',
        'id' : 'name'
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control text-left',
        'placeholder' : 'ایمیل',
        'id' : 'email'
    }), validators=[validators.EmailValidator])
    
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'شماره تماس',
        'id' : 'number'
    }), validators=[validators.MaxLengthValidator(12)])
    
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'توضیحات',
        'id' : 'content'
    }))