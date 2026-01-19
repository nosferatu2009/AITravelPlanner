import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCKiu0q3gZoas4UgpPacpGzCI86AjRD3tw")

model = genai.GenerativeModel("gemini-2.5-flash")

def llm(prompt: str) -> str:
    # for m in genai.list_models():
    #     if "generateContent" in m.supported_generation_methods:
    #         print(m.name)

    response = model.generate_content(prompt)
    return response.text
