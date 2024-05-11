import os
import uvicorn
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

from routers.spectrum import router as spectrum_router
from routers.hello import router as hello_router
from routers.spectrum_process import router as spectrum_process
from version import VERSION


'''
Load .env needed for project
'''
load_dotenv(find_dotenv())
ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME", None)

if (ENVIRONMENT_NAME is not None) and (ENVIRONMENT_NAME.startswith("Deploy")):
    # Disable swagger and redocs on deploy environment.
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI(title="API-Spectrum", description="API processamento sinais.", version=VERSION)


'''
Place to include the routes for this project
'''
app.include_router(spectrum_router, prefix="/spectrum", tags=["spectrum"])
app.include_router(hello_router, prefix="/hello", tags=["spectrum"])
app.include_router(spectrum_process, prefix="/spectrum_process", tags=["spectrum"])

'''
Swagger customization for better visual from API.
Use http:localhost:8000/docs for this
'''
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API-Spectrum",
        version=VERSION,
        description="API processamento sinais.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_schema="/openapi.json", title="API-Spectrum")


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(openapi_schema="/openapi.json", title="API-Spectrum")


@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_endpoint():
    return custom_openapi()


if __name__ == "__main__":
    API_PORT = os.getenv("API_PORT", 8000)
    uvicorn.run(main=app, port=int(API_PORT))
