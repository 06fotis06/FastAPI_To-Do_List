from fastapi import FastAPI

app = FastAPI()

# Список задач
tasks = []

# Модель задачи
class Task:
    def __init__(self, title: str):
        self.title = title
        self.completed = False

# Создание новой задачи
@app.post("/tasks/")
async def create_task(title: str):
    task = Task(title)
    tasks.append(task)
    return {"message": "Task created successfully", "task_title": title}

# Получение списка задач
@app.get("/tasks/")
async def get_tasks():
    return tasks

# Удаление задачи
@app.delete("/tasks/{task_index}")
async def delete_task(task_index: int):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        return {"message": "Task deleted successfully", "deleted_task": deleted_task.title}
    else:
        return {"message": "Task not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
