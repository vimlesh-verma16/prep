from enum import Enum
from datetime import datetime, timedelta
from threading import Lock
from collections import defaultdict
from typing import List, Optional
import uuid


# ---------------- Enums ---------------- #
class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


# ---------------- Models ---------------- #
class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.id = user_id
        self.name = name
        self.email = email


class Task:
    def __init__(
        self,
        task_id: str,
        title: str,
        description: str,
        due_date: datetime,
        priority: int,
        status: TaskStatus,
        assigned_user: User,
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.assigned_user = assigned_user
        self.created_at = datetime.now()


# ---------------- Singleton TaskManager ---------------- #
class TaskManager:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(TaskManager, cls).__new__(cls)
                    cls._instance._init_data()
        return cls._instance

    def _init_data(self):
        self.tasks = {}
        self.user_task_history = defaultdict(list)
        self._data_lock = Lock()

    def create_task(
        self,
        title: str,
        description: str,
        due_date: datetime,
        priority: int,
        assigned_user: User,
    ) -> Task:
        with self._data_lock:
            task_id = str(uuid.uuid4())
            task = Task(
                task_id,
                title,
                description,
                due_date,
                priority,
                TaskStatus.PENDING,
                assigned_user,
            )
            self.tasks[task_id] = task
            self.user_task_history[assigned_user.id].append(task)
            return task

    def update_task(
        self,
        task_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
        priority: Optional[int] = None,
        status: Optional[TaskStatus] = None,
    ) -> bool:
        with self._data_lock:
            task = self.tasks.get(task_id)
            if not task:
                return False
            if title:
                task.title = title
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if priority is not None:
                task.priority = priority
            if status:
                task.status = status
            return True

    def delete_task(self, task_id: str) -> bool:
        with self._data_lock:
            task = self.tasks.pop(task_id, None)
            if not task:
                return False
            self.user_task_history[task.assigned_user.id].remove(task)
            return True

    def search_tasks_by_user(self, user_id: str) -> List[Task]:
        return list(self.user_task_history.get(user_id, []))

    def filter_tasks(
        self,
        user_id: str,
        status: Optional[TaskStatus] = None,
        priority: Optional[int] = None,
    ) -> List[Task]:
        tasks = self.user_task_history.get(user_id, [])
        filtered = [
            task
            for task in tasks
            if (status is None or task.status == status)
            and (priority is None or task.priority == priority)
        ]
        return filtered

    def mark_task_completed(self, task_id: str) -> bool:
        return self.update_task(task_id, status=TaskStatus.COMPLETED)


# ---------------- Simulation ---------------- #
def simulate_task_system():
    manager = TaskManager()

    # Create users
    alice = User("u1", "Alice", "alice@example.com")
    bob = User("u2", "Bob", "bob@example.com")

    # Create tasks for Alice
    t1 = manager.create_task(
        "Write Report",
        "Finish annual report",
        datetime.now() + timedelta(days=2),
        1,
        alice,
    )
    t2 = manager.create_task(
        "Team Meeting", "Weekly sync", datetime.now() + timedelta(days=1), 2, alice
    )

    # Create tasks for Bob
    t3 = manager.create_task(
        "Deploy App",
        "Production deployment",
        datetime.now() + timedelta(days=3),
        1,
        bob,
    )
    t4 = manager.create_task(
        "Fix Bug", "Critical bug in payment", datetime.now() + timedelta(days=1), 1, bob
    )
    t5 = manager.create_task(
        "Write Tests", "Add unit tests", datetime.now() + timedelta(days=4), 3, bob
    )

    # Update status
    manager.update_task(t1.id, status=TaskStatus.IN_PROGRESS)
    manager.mark_task_completed(t2.id)
    manager.mark_task_completed(t4.id)

    # Delete a task
    manager.delete_task(t5.id)

    # View task history
    print("\n--- Alice's Task History ---")
    for task in manager.search_tasks_by_user(alice.id):
        print(f"{task.title} | Status: {task.status.value} | Priority: {task.priority}")

    print("\n--- Bob's Task History ---")
    for task in manager.search_tasks_by_user(bob.id):
        print(f"{task.title} | Status: {task.status.value} | Priority: {task.priority}")

    # Filter Bob's pending tasks
    print("\n--- Bob's PENDING Tasks ---")
    for task in manager.filter_tasks(bob.id, status=TaskStatus.PENDING):
        print(f"{task.title} | Due: {task.due_date.strftime('%Y-%m-%d')}")

    # Filter Alice’s high-priority tasks
    print("\n--- Alice's High Priority Tasks ---")
    for task in manager.filter_tasks(alice.id, priority=1):
        print(f"{task.title} | Status: {task.status.value}")


# Run the simulation
if __name__ == "__main__":
    simulate_task_system()
