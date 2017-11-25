from django import forms

class ContactForm(forms.Form):
    cname = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class':'form-control' ,'placeholder':'Name' }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type':'text','class':'form-control','placeholder':'Email'}))
    msg = forms.CharField(widget=forms.Textarea(attrs={'type':'text','class':'form-control','maxlength':150,'placeholder':'Message'}))
