from django import forms
from .models import Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())