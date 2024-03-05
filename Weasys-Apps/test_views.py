from django.test import TestCase
from django.urls import reverse
from .forms import ImageGeneratorForm
from openai import OpenAI

class ImageGeneratorViewTest(TestCase):
    def test_image_generator_view_with_valid_form(self):
        # Set the API key
        OpenAI.api_key = "YOUR_API_KEY"

        # Create a valid form data
        form_data = {
            'prompt': 'Test prompt',
        }

        # Send a POST request to the view
        response = self.client.post(reverse('image_generator'), data=form_data)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the image URL is present in the response context
        self.assertIn('image_url', response.context)

        # Assert that the image URL is not empty
        image_url = response.context['image_url']
        self.assertIsNotNone(image_url)
        self.assertNotEqual(image_url, '')

        # Assert that the image URL is displayed correctly on the template page
        self.assertContains(response, image_url)