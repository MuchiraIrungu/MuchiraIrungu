from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={
            'placeholder': 'Your Name',
            'minlength': '2',
            'required': 'true',
            'aria-required': 'true',
            'class': 'full-width',
        })
    )
    contact_email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'required': 'true',
            'aria-required': 'true',
            'class': 'full-width',
        })
    )
    contact_subject = forms.CharField(max_length=200, label='Subject',required=False,widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'full-width',
        })
    )
    contact_message = forms.CharField( widget=forms.Textarea(attrs={
            'placeholder': 'Your Message',
            'rows': '10',
            'cols': '50',
            'required': 'true',
            'aria-required': 'true',
            'class': 'full-width',
        })
    )