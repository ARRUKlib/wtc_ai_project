# === modules/rag.py ===
import requests

def get_context_from_openai_api(question: str) -> str:
    url = "https://your-openai-backend-api.com/rag"
    response = requests.post(url, json={"question": question})
    if response.status_code == 200:
        return response.json().get("context", "")
    return "ไม่พบข้อมูลจากระบบ"
