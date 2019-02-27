from django import forms
from .models import BlogPost

# Model Form
class NewBlogPost(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ['title', 'text']
