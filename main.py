from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"status": "organism online"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return {"alive": True}
