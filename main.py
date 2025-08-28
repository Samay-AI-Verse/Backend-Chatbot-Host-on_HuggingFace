from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Hugging Face FastAPI!"}

@app.post("/predict")
def predict(data: dict):
    text = data.get("text", "")
    return {"reversed_text": text[::-1]}
