from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from services.hello_service.srv_hello import get_hello_message

router = APIRouter()

@cbv(router)
class HelloWorld:
    @router.get("/")
    async def hello_world(self):
        return {"message": get_hello_message()}
