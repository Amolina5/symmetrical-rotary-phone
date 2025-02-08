from flask import (
    Flask,
    request
)
from app.database import task

app = Flask(__name__)

# rest respresentaion state transfer
# rest is an architectual desing pattren that helps design out API services
@app.get("/")
@app.get("/tasks")
def get_all_task():
    out = {
        "task": task.scan(),
        "ok": True
    }
    return out

@app.get("/task/<int:pk>")
def get_single_task(pk):
    out = {
        "task": task.select_by_id(pk),
        "ok": True
    }
    return out

@app.put("/task/<int:pk>")
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204

@app.post("/tasks")
def add_task():
    task_data = request.json
    task.insert_task(task_data)
    return "", 201

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204

# @app.post("/tasks") # this route should be mapped to a function that creates new tasks
# @app.put ("/tasks/<int:pk>") # this route should be mapped to a function that updates exting tasks
#@app.delete("/tasks/<int:pk>") # this route should be mapped to a function that deletes existing tasks

#youll also the request context object.
# you can retruce the income JSON from the request body by using request.JSON

""" 
{
    "name": "task name",
    "summary: "task summary",
    "descrition: "task description"
}
"""