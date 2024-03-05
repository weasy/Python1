import os
import openai
import webbrowser
openai.api_key = os.environ["OPENAI_API_KEY"]
class ImageGenerator:
    def __init__(self, prompt: str, model: str):
        self.openai = openai
        self.prompt = prompt
        self.model = model
        self.link = None  # Initialize the link attribute

    def generate_image(self) -> None:
        response = self.openai.images.generate(prompt=self.prompt, model=self.model)
        return response

prompt = input("Enter what crazy crap you want to see: ")
model = "dall-e-3"
image_generator = ImageGenerator(prompt, model)
response = image_generator.generate_image()

# Check if response is None
if response is None:
    print("Failed to generate image. Please check your prompt and model.")
else:
    # Print the link
    image_url = response.data[0].url
    print("Image URL:", image_url)

    # Open the link in Edge
    webbrowser.open(image_url)
