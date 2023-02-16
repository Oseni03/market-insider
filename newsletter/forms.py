from django import forms

from .models import Newsletter 

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter 
        fields = ('email',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})