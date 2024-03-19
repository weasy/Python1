from django import forms

class ImageGeneratorForm(forms.Form):
    prompt = forms.CharField(widget=forms.Textarea, required=True)