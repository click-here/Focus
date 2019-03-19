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
    def __init__(self, text, task_family):
        self.createdon = datetime.datetime.now()
        self.text = text
        self.is_active = True
        self.task_family = task_family
        task_family.add_task(self)
        
    # def assign_task_family(self, task_family):
        


class TaskFamily:
    def __init__(self, name):
        self.createdon = datetime.datetime.now()
        self.name = name
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

class Client(TaskFamily):

    def __init__(self, name, client):
        super().__init__(name)
        self.client = client


    

tf1 = TaskFamily('Personal')
t1 = Task('go to the store for eggs', tf1)
