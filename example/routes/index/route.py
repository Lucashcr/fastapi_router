from fastapi import Request

async def get(request: Request):
    return {"message": "GET /blog/get"}

async def post(request: Request):
    return {"message": "POST /blog/post"}
