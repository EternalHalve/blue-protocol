from fastapi import FastAPI

from api import grass_finder

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Hello World"}

app.include_router(grass_finder.router, prefix="/api")