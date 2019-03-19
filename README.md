# Focus
Complete reenvisioning of my project "Current Task"


# Usage

```python
tf1 = TaskFamily('Personal')
t1 = Task('go to the store for eggs', tf1)

tf2 = Client('Work', 'Celestial Wealth Coffee')
t2 = Task('email tim',tf2)
t3 = Task('email sue',tf2)

print(t1.text)
>>> 'go to the store for eggs'

print(t1.task_family.name)
>>> 'Personal'


print(t2.text)
>>> 'email tim'

print(t2.task_family.name)
>>> 'Work'

print(t2.task_family.client)
>>> 'Celestial Wealth Coffee'


print(tf2.last_task().text)
>>> 'email sue'
```