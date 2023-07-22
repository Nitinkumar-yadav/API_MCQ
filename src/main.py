from fastapi import FastAPI
import uvicorn
from generative_ai.routes import router
from utils.logger import logManager

logger = logManager()

app =FastAPI()
app.include_router(router)

if __name__ == "__main__":
     logger.info("Starting Application")
     uvicorn.run(app, host="localhost", port=8080)