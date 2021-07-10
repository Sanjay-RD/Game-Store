from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    blogDescription = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = ['blogTitle','blogDescription','blogImage']
