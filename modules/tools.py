# === modules/tools.py ===
from langchain.agents import Tool

def ToolRouter():
    def calculator_run(input_text):
        try:
            return str(eval(input_text))
        except Exception as e:
            return f"Error: {e}"

    return [
        Tool(name="Calculator", func=calculator_run, description="ใช้คำนวณเลข")
    ]