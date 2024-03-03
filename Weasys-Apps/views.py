import os
import sys
import openai
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageGeneratorForm

openai.api_key = os.environ["OPENAI_API_KEY"]

class ImageGenerator:
    def __init__(self, prompt: str, model: str):
        self.openai = openai
        self.prompt = prompt
        self.model = model

    def generate_image(self) -> None:
        response = self.openai.images.generate(prompt=self.prompt, model=self.model)
        return response

def image_generator_view(request):
    if request.method == 'POST':
        form = ImageGeneratorForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            model = "dall-e-3"
            image_generator = ImageGenerator(prompt, model)
            response = image_generator.generate_image()
            if response is not None:
                image_url = response.data[0].url
                return render(request, 'image_generator.html', {'form': form, 'image_url': image_url})
    else:
        form = ImageGeneratorForm()
    return render(request, 'image_generator.html', {'form': form})
