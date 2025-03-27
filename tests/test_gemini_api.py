from google import genai

client = genai.Client(api_key="AIzaSyAsprkYRP3oXxyY-Qcxhz6qYH70HL0Gvjw")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)