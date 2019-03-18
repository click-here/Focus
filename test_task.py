import unittest
import task
import datetime
import time


class TestTask(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.basic_task = task.Task('Watch that movie')
        self.work_task = task.WorkTask('Email that person','Celestial Wealth Coffee')
    
    def tearDown(self):
        pass
    
    def test_create_task(self):
        self.assertEqual(self.basic_task.text, 'Watch that movie')
        self.assertGreaterEqual(self.basic_task.createdon, datetime.datetime.now())
        self.assertTrue(self.basic_task.is_active)

    def test_create_work_task(self):
        self.assertEqual(self.work_task.text, 'Email that person')
        self.assertEqual(self.work_task.client, 'Celestial Wealth Coffee')
        self.assertGreaterEqual(self.work_task.createdon, datetime.datetime.now())
        self.assertTrue(self.work_task.is_active)


class TestTaskList(unittest.TestCase):

    def setUp(self):
        self.task1 = task.Task('Watch that movie')
        
    def test_create_tasklist(self):
        mytasks = task.TaskList()
        self.assertGreaterEqual(mytasks.createdon, datetime.datetime.now())
        self.assertEqual(mytasks.tasks, [])

    def test_add_one_task(self):
        short_task_list = task.TaskList()
        short_task_list.add(self.task1)
        self.assertEqual(len(short_task_list.tasks), 1)
    
    def test_last_added_and_multiple_added(self):
        self.task2 = task.Task('Watch that tv show')
        self.task3 = task.Task('Listen to that song')
        self.worktask1 = task.WorkTask('Email that person', 'Celestial Wealth Coffee')
        time.sleep(1/10000000)       
        worktask2 = task.WorkTask('Call Taylor', 'Dark as Bark Coffee')
        
        self.task_list_for_checking_methods = task.TaskList()
        self.task_list_for_checking_methods.add([self.task1, self.task2, self.task3, self.worktask1, worktask2])

        last_task = self.task_list_for_checking_methods.last_task()

        self.assertEqual(last_task.text, 'Call Taylor')
        self.assertEqual(len(self.task_list_for_checking_methods.tasks),5)




if __name__ == "__main__":
    unittest.main()