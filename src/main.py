import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=80, reload=True, log_level="info")
