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
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def frontend():
    return FileResponse(os.path.join(os.getcwd(), "index.html"))
@app.get("/status")
def status():
    return {"alive": True}
