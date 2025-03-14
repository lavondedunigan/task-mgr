from flask import Flask, request
from app.database import task

app = Flask("_name_")

# REST - Representational State Transfer
# Rest is an architectual design pattern for building network-connected services.

@app.get("/")
@app.get("/tasks")
def get_tasks():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out

@app.get("/tasks/<int:pk>/")
def get_single_task(pk):
    out = {
        "task": task.select_by_id(pk),
        "ok": True
    }
    return out

@app.post("/tasks")
def create_task():
    task.create_task(request.json)
    return "", 204

@app.put("/tasks/<int:pk>/")
def update_task(pk):
    task.update_task_by_id(request.json,pk)
    return "", 204


@app.delete("/tasks/<int:pk>/")
def delete_task(pk):
    task.delete_task_by_id(request.json,pk)
    return "", 204


    