import google.generativeai as genai
import json
from src.config.settings import settings

def find_company_info_FreeGemini(company_name: str, data: dict) -> dict:
    try:
        genai.configure(api_key=settings.google_api_key)
        MODEL_NAME = 'gemini-2.0-pro-exp'
        model = genai.GenerativeModel(MODEL_NAME)

        prompt = (
            f"Please complete the following information about {company_name} in JSON format only (no explanations or extra text): {data}"
        )

        response = model.generate_content(prompt)
        data = json.loads(response.text.replace("```json", "").replace("```", ""))
        return data
    except Exception as e:
        print(f"❌ Failed to call Gemini API: {e}")
        return None