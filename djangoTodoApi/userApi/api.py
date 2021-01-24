from datetime import date
from django.contrib.auth.models import User
from typing import List
from ninja import Router, Schema
from django.shortcuts import get_object_or_404
from .models import UserProfile

router = Router()

# For User
class UserIn(Schema):
    username: str
    password: str 
    email: str 

class UserOut(Schema):
    id: int
    username: str
    password: str 
    email: str 

@router.get("/", response=List[UserOut], tags=["Users"])
def list_users(request):
    qs = User.objects.all()
    return qs

@router.get("/{user_id}", response=UserOut, tags=["Users"])
def get_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    return user

@router.post("/", tags=["Users"])
def create_user(request, payload: UserIn):
    user = User.objects.create(**payload.dict())
    return {"id": user.id}

@router.delete("/{user_id}", tags=["Users"])
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return {"success": True}

@router.put("/{user_id}", tags=["Users"])
def update_user(request, user_id: int, payload: UserIn):
    user = get_object_or_404(User, id=user_id)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    return {"success": True}
