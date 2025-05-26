from django import forms
from home.models import ContactUs, Comments


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','content','email')


