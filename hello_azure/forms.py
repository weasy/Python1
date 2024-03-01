from django import forms

class ImageGeneratorForm(forms.Form):
    prompt = forms.CharField(label='Enter what crazy crap you want to see', max_length=100)