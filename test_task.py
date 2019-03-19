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
        self.tf1 = task.TaskFamily('Personal')
        self.t1 = task.Task('go to the store for eggs', self.tf1)

        self.tf2 = task.Client('Work', 'Celestial Wealth Coffee')
        self.t2 = task.Task('Email that person',self.tf2)  

    def tearDown(self):
        pass
    
    def test_create_task(self):
        self.assertEqual(self.t1.text, 'go to the store for eggs')
        self.assertGreaterEqual(self.t1.createdon, datetime.datetime.now())
        self.assertTrue(self.t1.is_active)

    def test_create_work_task(self):
        self.assertEqual(self.t2.text, 'Email that person')
        self.assertEqual(self.t2.task_family.client, 'Celestial Wealth Coffee')
        self.assertGreaterEqual(self.t2.createdon, datetime.datetime.now())
        self.assertTrue(self.t2.is_active)

class TestTaskFamily(unittest.TestCase):

    def setUp(self):
        self.tf1 = task.TaskFamily('Personal')
        self.t1 = task.Task('go to the store for eggs', self.tf1)

        self.tf2 = task.Client('Work', 'Celestial Wealth Coffee')
        self.t2 = task.Task('Email that person',self.tf2) 

    def test_last_added(self):
        time.sleep(1/10000000)
        self.t1 = task.Task('should be last task', self.tf1)
        last_task = self.tf1.last_task()
        self.assertEqual(last_task.text, 'should be last task')
    
    def test_client(self):
        client = self.t2.task_family.client
        self.assertEqual(client, 'Celestial Wealth Coffee')




if __name__ == "__main__":
    unittest.main()