from django import forms

class UserCreationForm(forms.Form):
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'class':'su-field', 'placeholder':'Email'}))
    username = forms.CharField(label=False, min_length=3, max_length=20, widget=forms.TextInput(attrs={'class':'su-field', 'placeholder':'Username'}))
    password = forms.CharField(label=False, min_length=6, max_length=20, widget=forms.TextInput(attrs={'class':'su-field', 'placeholder':'Password (6 Characters Minimum)', 'type':'password'}))

class LogInForm(forms.Form):
    username = forms.CharField(label=False, min_length=3, max_length=20, widget=forms.TextInput(attrs={'class':'su-field', 'placeholder':'Username'}))
    password = forms.CharField(label=False, min_length=6, max_length=20, widget=forms.TextInput(attrs={'class':'su-field', 'placeholder':'Password', 'type':'password'}))

class MediaForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=400)
    duration = forms.FloatField()
    image_filepath = forms.CharField(max_length=100)
    quiz_type = forms.CharField(max_length=30)