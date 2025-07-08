# sourcecodeAgent

### 

```bash
mkdir code-review-agent
cd code-review-agent
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pydantic aiohttp
```

### 해결 방법 (단 1회만 등록 진행)

### 1. ngrok 계정 생성

👉 https://dashboard.ngrok.com/signup

- 무료 플랜으로 가입 가능
- 이메일 인증까지 완료

---

### 2. 인증 토큰 복사

👉 https://dashboard.ngrok.com/get-started/your-authtoken

예시:

```
markdown
복사편집
ngrok config add-authtoken 2Pb***************R45

```

---

### 3. 터미널에서 등록

```bash
bash
복사편집
ngrok config add-authtoken <복사한_토큰>

```

---

### 4. 다시 실행

```bash
bash
복사편집
ngrok http 8000

```