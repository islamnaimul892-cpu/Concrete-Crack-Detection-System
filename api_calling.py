from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = my_api_key)

def content_generator(images):
    promt = """You are a civil infrastructure inspection expert.

    Analyze the uploaded concrete image.

    Identify:
    1. Presence of cracks
    2. Crack type
    3. Severity level
    4. Possible causes
    5. Structural risk
    6. Repair recommendation

    Severity Levels:
    - Minor
    - Moderate
    - Severe

    Generate professional engineering inspection comments."""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images,promt]
    )
    return response.text



