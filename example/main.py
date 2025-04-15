from fastapi import FastAPI
from fastapi_autorouter import auto_load_routes

app = FastAPI()
auto_load_routes(app, "example/routes")
