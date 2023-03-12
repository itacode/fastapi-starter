import uvicorn


def start():
    uvicorn.run("app.main:app", reload=True)
