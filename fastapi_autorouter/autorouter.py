import os
import importlib.util
import inspect
from typing import Optional

from fastapi import FastAPI, APIRouter

from fastapi_autorouter.utils.constants import HTTP_METHODS
from fastapi_autorouter.utils.helpers import convert_path, extract_tag


def auto_load_routes(app: FastAPI, routes_dir: Optional[str] = None):
    if routes_dir is None:
        caller_file = inspect.stack()[1].filename
        base_dir = os.path.dirname(caller_file)
        routes_dir = os.path.join(base_dir, "routes")

    for root, _, files in os.walk(routes_dir):
        for file in files:
            if file != "route.py":
                continue

            module_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, routes_dir)
            route_path = convert_path(relative_path)
            route_tag = extract_tag(relative_path)

            spec = importlib.util.spec_from_file_location("route", module_path)
            if spec is None or spec.loader is None:
                raise RuntimeError(f"Failed to get spec from {module_path}")

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            router = APIRouter()

            for attr_name in dir(module):
                if attr_name in HTTP_METHODS:
                    endpoint = getattr(module, attr_name)
                    router.add_api_route(
                        path="/",
                        endpoint=endpoint,
                        methods=[attr_name.upper()],
                    )

            app.include_router(
                router,
                prefix=route_path if route_path != "/" else "",
                tags=[route_tag]
            )
