from ninja import NinjaAPI
from todoApi.api import router as todos_router
from userApi.api import router as users_router
from userApi.api2 import router as profiles_router
from ninja.security import HttpBasicAuth
from ninja.security import HttpBearer

# class BasicAuth(HttpBasicAuth):
#     def authenticate(self, request, username, password):
#         if username == "admin" and password == "secret":
#             return username

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "code":
            return token

api = NinjaAPI()
# api = NinjaAPI(auth=GlobalAuth(), csrf=True)

api.add_router("/todos/", todos_router)
api.add_router("/users/", users_router)
api.add_router("/profiles/", profiles_router)

# @api.get("/intro", tags=["Intro"])
# def hello(request):
#     return "Hellow, Welcome To Django-Ninja"
  

