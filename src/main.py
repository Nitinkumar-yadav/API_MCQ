from fastapi import FastAPI
import uvicorn
from generative_ai.routes import router

app =FastAPI()
app.include_router(router)


if __name__ == "__main__":
     uvicorn.run(app, host="localhost", port=8080)