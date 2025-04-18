# === main.py ===
from fastapi import FastAPI, Request
from langchain.llms import LlamaCpp
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from modules.tools import ToolRouter
from modules.rag import get_context_from_openai_api

llm = LlamaCpp(
    model_path="./models/deepseek-r1.gguf",
    temperature=0.3,           # 👈 ควบคุมความ "หลุดโลก"
    top_p=0.8,                 # 👈 ความหลากหลาย (nucleus sampling)
    top_k=40,                  # 👈 กรอง token ที่มีโอกาสน้อย
    max_tokens=1024,           # 👈 จำกัดความยาวของคำตอบ
    repeat_penalty=1.1,        # 👈 ป้องกันคำซ้ำ
    n_batch=64,                # 👈 batch size ขณะรัน
    n_gpu_layers=32,           # 👈 ใช้ GPU ได้ถ้ามี (สำหรับ RunPod)
    verbose=True
)


memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory)

app = FastAPI()

@app.post("/ask")
async def ask_user(request: Request):
    body = await request.json()
    question = body.get("question", "")
    context = get_context_from_openai_api(question)
    response = chain.predict(input=f"Context: {context}\nQuestion: {question}")
    return {"answer": response}