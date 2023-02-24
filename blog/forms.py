from django import forms 

from .models import ContactMessage

class AdminMailer(forms.Form):
    user = forms.ModelChoiceField(queryset=ContactMessage.objects.all(), empty_label="Select contact message")
    message = forms.CharField(widget=forms.Textarea(attrs={'size': '10', "class": "form-control"}))
    
    user.widget.attrs.update({'class': 'form-select'})