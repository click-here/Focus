import datetime

class TaskList:

    def __init__(self):
        self.createdon = datetime.datetime.now()
        self.tasks = []

    def add(self, task):
        """Expects 1 or more Task class object"""
        if isinstance(task, Task):
            self.tasks.append(task)
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

mytasks = TaskList()
# Add tasks individually
mytasks.add(Task('get eggs'))
mytasks.add(Task('call mom back'))
mytasks.add(WorkTask('send that email to tim','Celestial Wealth Coffee'))

# Add a batch of tasks
t1 = Task('watch that movie')
t2 = Task('buy oil for car')
t3 = Task('pick up library book')

tasks_to_add = [t1,t2,t3]

mytasks.add(tasks_to_add)

mytasks.show_tasks()
