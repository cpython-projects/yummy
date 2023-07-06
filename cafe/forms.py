from django import forms
from captcha.fields import ReCaptchaField
from .models import BookTable


class ContactForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'id': 'name',
                                                                       'placeholder': 'Your Name',
                                                                       'required': 'true'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'id': 'email',
                                                                           'placeholder': 'Your Email',
                                                                           'required': 'true'}))
    subject = forms.CharField(label='subject', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'id': 'subject',
                                                                             'placeholder': 'Subject',
                                                                             'required': 'true'}))
    message = forms.CharField(label='message', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                            'rows': 5,
                                                                            'id': 'message',
                                                                            'placeholder': 'Message',
                                                                            'required': 'true'}))
    captcha = ReCaptchaField()


class BookTableForm(forms.ModelForm):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Your Name',
                                                                       'class': 'form-control',
                                                                       'id': 'name',
                                                                       'data-rule': 'minlen:4',
                                                                       'data-msg': 'Please enter at least 4 chars'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                           'class': 'form-control',
                                                                           'id': 'email',
                                                                           'data-rule': 'email',
                                                                           'data-msg': 'Please enter a valid email'}))
    phone = forms.CharField(label='phone', widget=forms.TextInput(attrs={'placeholder': 'Your Phone',
                                                                         'class': 'form-control',
                                                                         'id': 'phone',
                                                                         'data-rule': 'minlen:4',
                                                                         'data-msg': 'Please enter a valid phone: +38(0xx)xxxxxxx'}))
    date = forms.DateField(label='date', widget=forms.DateInput(attrs={'placeholder': 'Date (YYYY-MM-DD)',
                                                                       'class': 'form-control',
                                                                       'id': 'date',
                                                                       'data-rule': 'minlen:4',
                                                                       'data-msg': 'Please enter at least 4 chars'}))
    time = forms.TimeField(label='time', widget=forms.TimeInput(attrs={'placeholder': 'Time (HH:MM)',
                                                                       'class': 'form-control',
                                                                       'id': 'time',
                                                                       'data-rule': 'minlen:2',
                                                                       'data-msg': 'Please enter at least 2 chars'}))
    people = forms.IntegerField(label='people', widget=forms.NumberInput(attrs={'placeholder': '# of people',
                                                                                'class': 'form-control',
                                                                                'id': 'people',
                                                                                'data-rule': 'minlen:1'}))
    message = forms.CharField(label='message',widget=forms.Textarea(attrs={'placeholder': 'Message',
                                                                           'class': 'form-control',
                                                                           'rows': '5'}))
    captcha = ReCaptchaField()

    class Meta:
        model = BookTable
        fields = ('name', 'email', 'phone', 'date', 'time', 'people', 'message')
