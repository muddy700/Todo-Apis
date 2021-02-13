from datetime import date
from typing import List
from ninja import Router, Schema
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Todo


router = Router()

class TodoIn(Schema):
    title: str
    description: str
    owner_id: int 
    status: str

class TodoOut(Schema):
    id: int
    title: str
    description: str
    date_created: date 
    owner_id: int
    status: str

# For Todo

@router.get("/", response=List[TodoOut], tags=["Todos"])
def list_todos(request):
    qs = Todo.objects.all()
    return qs

@router.get("/{todo_id}", response=TodoOut, tags=["Todos"])
def get_todo(request, todo_id: int):
    todo = get_object_or_404(Todo, id=todo_id)
    return todo

@router.post("/create/", tags=["Todos"])
def create_todo(request, payload: TodoIn):
    todo = Todo.objects.create(**payload.dict())
    return {"id": todo.id}

@router.delete("/delete/{todo_id}", tags=["Todos"])
def delete_todo(request, todo_id: int):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return {"success": True}

@router.put("/update/{todo_id}", tags=["Todos"])
def update_todo(request, todo_id: int, payload: TodoIn):
    todo = get_object_or_404(Todo, id=todo_id)
    for attr, value in payload.dict().items():
        setattr(todo, attr, value)
    todo.save()
    return {"success": True}

# Todo Filters
@router.get("/user/{user_id}", response=List[TodoOut], tags=["Filters"])
def list_user_todos(request, user_id: int):
    qs = Todo.objects.filter(owner_id=user_id)
    return qs

@router.get("/completed/", response=List[TodoOut], tags=["Filters"])
def completed_todos(request):
    qs = get_list_or_404(Todo, status=True)
    return qs

@router.get("/pending/", response=List[TodoOut], tags=["Filters"])
def pending_todos(request):
    qs = get_list_or_404(Todo, status=False)
    return qs