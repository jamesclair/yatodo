from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/")
async def read_tasks():
    return {"Hello": "World"}
