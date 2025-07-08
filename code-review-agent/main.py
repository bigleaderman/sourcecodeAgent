from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    headers = request.headers
    event = headers.get("X-GitHub-Event")
    payload = await request.json()

    print(f"📬 Received event: {event}")
    print(json.dumps(payload, indent=2))  # 로그로 확인용

    return {"status": "ok"}
