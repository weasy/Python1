import os
import openai as OpenAI
from django.shortcuts import render
from .forms import ImageGeneratorForm

OpenAI.api_key = os.environ["OPENAI_API_KEY"]

def generate_image(prompt: str, model: str) -> None:
    client = OpenAI()
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response

def image_generator_view(request):
    if request.method == 'POST':
        form = ImageGeneratorForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            model = "dall-e-3"
            response = generate_image(prompt, model)
            if response is not None:
                image_url = response.data[0].url
                return render(request, 'Weasys-Apps/image_generator.html', {'form': form, 'image_url': image_url})
        else:
            form = ImageGeneratorForm()
    else:
        form = ImageGeneratorForm()
    return render(request, 'Weasys-Apps/image_generator.html', {'form': form})
