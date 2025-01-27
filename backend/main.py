from fastapi import FastAPI
from pydantic import BaseModel
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (보안을 위해 특정 도메인만 허용할 수 있음)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 요청 헤더 허용
)

# 모델 정의 (예시로 "message"와 "count" 값을 반환)
class ResponseModel(BaseModel):
    message: str
    count: int

@app.get("/")
async def greet():
    return ("Hello welcome!")
@app.get("/api/random-message", response_model=ResponseModel)
async def random_message():
    messages = ["Hello, World!", "FastAPI is awesome!", "React and FastAPI FTW!"]
    random_message = random.choice(messages)
    return ResponseModel(message=random_message, count=random.randint(1, 100))
