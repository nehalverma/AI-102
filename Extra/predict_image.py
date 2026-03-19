from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

# ✅ Use your Prediction endpoint and key (not Training)
PREDICTION_ENDPOINT = ""
PREDICTION_KEY =""

# ✅ Your project and published model name
PROJECT_ID =""
MODEL_NAME = ""   # Must match the published iteration name in Custom Vision

# Authenticate client
credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
prediction_client = CustomVisionPredictionClient(endpoint=PREDICTION_ENDPOINT,
                                                 credentials=credentials)

# Load image
with open("mango.jpeg", "rb") as image_file:
    image_data = image_file.read()

# Classify image
response = prediction_client.classify_image(PROJECT_ID, MODEL_NAME, image_data)

# Print predictions
print("Prediction results:")
for prediction in response.predictions:
    print(f"{prediction.tag_name}: {prediction.probability:.2f}")