from django import forms



class CommentForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'نام',
        'id' : 'reply-name'
    }))
    
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control mb-4',
        'placeholder' : 'کامنت',
        'id' : 'reply-massage'
    }))