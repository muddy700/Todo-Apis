from datetime import date
from django.contrib.auth.models import User
from typing import List
from ninja import Router, Schema
from django.shortcuts import get_object_or_404
from .models import UserProfile

router = Router()


# For UserPrpfile
class ProfileIn(Schema):
    user_id: int
    image: str = None
    phone: str

class ProfileOut(Schema):
    id: int
    user_id: int
    image: str = None
    phone: str 

@router.get("/", response=List[ProfileOut], tags=["User Profile"])
def list_users_Profiles(request):
    qs = UserProfile.objects.all()
    return qs

@router.get("/{profile_id}", response=ProfileOut, tags=["User Profile"])
def get_single_Profile(request, profile_id: int):
    profile = get_object_or_404(UserProfile, id=profile_id)
    return profile

@router.get("/user/{owner_id}", response=ProfileOut, tags=["Filters"])
def get_user_Profile(request, owner_id: int):
    profile = get_object_or_404(UserProfile, user_id=owner_id)
    return profile

@router.post("/create/", tags=["User Profile"])
def create_user_Profile(request, payload: ProfileIn):
    profile = UserProfile.objects.create(**payload.dict())
    return {"id": profile.id}

@router.delete("/delete/{profile_id}", tags=["User Profile"])
def delete_user_Profile(request, profile_id: int):
    profile = get_object_or_404(UserProfile, id=profile_id)
    profile.delete()
    return {"success": True}

@router.put("/update/{profile_id}", tags=["User Profile"])
def update_user_Profile(request, profile_id: int, payload: ProfileIn):
    profile = get_object_or_404(UserProfile, id=profile_id)
    for attr, value in payload.dict().items():
        setattr(profile, attr, value)
    profile.save()
    return {"success": True}

