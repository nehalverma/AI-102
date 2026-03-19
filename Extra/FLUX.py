# Install required packages: `pip install requests pillow azure-identity`
import os
import requests
import base64
from PIL import Image
from io import BytesIO
from azure.identity import DefaultAzureCredential

# You will need to set these environment variables or edit the following values.
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")
deployment = os.getenv("DEPLOYMENT_NAME", "FLUX.1-Kontext-pro")
api_version = os.getenv("OPENAI_API_VERSION", "2025-04-01-preview")

def decode_and_save_image(b64_data, output_filename):
  image = Image.open(BytesIO(base64.b64decode(b64_data)))
  image.show()
  image.save(output_filename)

def save_response(response_data, filename_prefix):
  data = response_data['data']
  b64_img = data[0]['b64_json']
  filename = f"{filename_prefix}.png"
  decode_and_save_image(b64_img, filename)
  print(f"Image saved to: '{filename}'")

# Initialize the DefaultAzureCredential to be used for Entra ID authentication.
# If you receive a `PermissionDenied` error, be sure that you run `az login` in your terminal
# and that you have the correct permissions to access the resource.
# Learn more about necessary permissions:  https://aka.ms/azure-openai-roles
credential = DefaultAzureCredential()
token_response = credential.get_token("https://cognitiveservices.azure.com/.default")

base_path = f'openai/deployments/{deployment}/images'
params = f'?api-version={api_version}'

generation_url = f"https://foundry-new-01.cognitiveservices.azure.com/{base_path}/generations{params}"
generation_body = {
  "prompt": "A flower farm with colorful flowers growing in neat rows under a blue sky",
  "n": 1,
  "size": "1024x1024",
  "output_format": "png"
}
generation_response = requests.post(
  generation_url,
  headers={
    'Authorization': 'Bearer ' + token_response.token,
    'Content-Type': 'application/json',
  },
  json=generation_body
).json()
save_response(generation_response, "generated_image")

# In addition to generating images, you can edit them.
edit_url = f"{endpoint}{base_path}/edits{params}"
edit_body = {
  "prompt": "A flower farm with colorful flowers growing in neat rows under a blue sky",
  "n": 1,
  "size": "1024x1024"
}
files = {
  "image": ("generated_image.png", open("generated_image.png", "rb"), "image/png"),
}
edit_response = requests.post(
  edit_url,
  headers={'Authorization': 'Bearer ' + token_response.token},
  data=edit_body,
  files=files
).json()
save_response(edit_response, "edited_image")