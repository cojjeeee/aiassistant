import os

from django.shortcuts import render
from google import genai


def home(request):
    response_text = ""

    if request.method == "POST":
        prompt = request.POST.get("prompt", "").strip()

        if prompt:
            try:
                client = genai.Client(
                    api_key=os.getenv("GEMINI_API_KEY")
                )

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                response_text = response.text or "No response was returned."

            except Exception as e:
                response_text = f"Error: {e}"

    return render(request, "home.html", {
        "response_text": response_text
    })