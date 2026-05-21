from typing import Callable, List, Awaitable

task_completed_callbacks: List[Callable[[dict], Awaitable[None]]] = []

def register_task_completed_callback(func):
    task_completed_callbacks.append(func)

async def trigger_task_completed(task: dict):
    for callback in task_completed_callbacks:
        await callback(task)