import datetime

class Task:
    def __init__(self, text, task_family):
        self.createdon = datetime.datetime.now()
        self.text = text
        self.is_active = True
        self.task_family = task_family
        task_family.add_task(self)

class TaskFamily:
    def __init__(self, name):
        self.createdon = datetime.datetime.now()
        self.name = name
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

    def last_task(self):
        return max(self.tasks, key=lambda item: item.createdon)

class Client(TaskFamily):

    def __init__(self, name, client):
        super().__init__(name)
        self.client = client