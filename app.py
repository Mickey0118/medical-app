from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# 允许跨域访问（CORS 解决方案）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源（可以改成具体的域名）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有请求头
)

@app.get("/")
def read_root():
    return {"message": "Hello, 你的 API 运行成功啦！"}

@app.get("/query")
def query_disease(symptom: str):
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()
    cursor.execute("SELECT disease, probability FROM symptom_disease WHERE symptom = ?", (symptom,))
    results = cursor.fetchall()
    conn.close()
    return [{"disease": d, "probability": p} for d, p in results]

