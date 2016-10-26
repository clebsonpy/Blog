from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['titulo', 'texto']
        labels = {'titulo': 'Titulo' ,'texto':''}
        widgets = {'texto': forms.Textarea(attrs={'cols':80})}