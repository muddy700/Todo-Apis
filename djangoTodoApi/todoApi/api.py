from datetime import date
from typing import List
from ninja import Router, Schema
from django.shortcuts import get_object_or_404
from .models import Todo


router = Router()

class TodoIn(Schema):
    title: str
    description: str
    owner_id: int 

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

@router.post("/", tags=["Todos"])
def create_todo(request, payload: TodoIn):
    todo = Todo.objects.create(**payload.dict())
    return {"id": todo.id}

@router.delete("/{todo_id}", tags=["Todos"])
def delete_todo(request, todo_id: int):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return {"success": True}

@router.put("/{todo_id}", tags=["Todos"])
def update_todo(request, todo_id: int, payload: TodoIn):
    todo = get_object_or_404(Todo, id=todo_id)
    for attr, value in payload.dict().items():
        setattr(todo, attr, value)
    todo.save()
    return {"success": True}