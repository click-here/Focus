import datetime

class TaskList:

    def __init__(self):
        self.createdon = datetime.datetime.now()
        self.tasks = []

    def add(self, task):
        """Expects 1 or more Task class object"""
        if isinstance(task, Task):
            self.tasks.append(task)
        elif isinstance(task, str):
            self.tasks.append(Task(task))
        else:
            for t in task:
                self.tasks.append(t)

    def last_task(self):
        return max(self.tasks, key=lambda item: item.createdon)
    
    def show_tasks(self):
        for t in self.tasks:
            print(t.text)

class Task:
    def __init__(self, text):
        self.createdon = datetime.datetime.now()
        self.text = text
        self.is_active = True

class WorkTask(Task):
    def __init__(self, task, client):
        super().__init__(task)
        self.client = client

