import os
from django.shortcuts import render
from .forms import ImageGeneratorForm
import openai

# Set the API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

def image_generator_view(request):
    if request.method == 'POST':
        form = ImageGeneratorForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            model = "dall-e-3"
            try:
                response = openai.images.generate(
                    model=model,
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )
                if response is not None:
                    image_url = response.data[0].url
                    return render(request, 'Weasys-Apps/image_generator.html', {'form': form, 'image_url': image_url})
            except Exception as e:
                print(f"Error during image generation: {e}")
                # Handle other exceptions (e.g., log the error)
    else:
        form = ImageGeneratorForm()
    return render(request, 'Weasys-Apps/image_generator.html', {'form': form})
