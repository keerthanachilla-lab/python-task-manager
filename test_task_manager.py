import unittest
from unittest.mock import patch
import task_manager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        task_manager.tasks.clear()

    @patch("builtins.input", return_value="Study Python")
    def test_add_task(self, mock_input):
        task_manager.add_task()
        self.assertIn("Study Python", task_manager.tasks)

    def test_view_tasks_empty(self):
        task_manager.view_tasks()
        self.assertEqual(task_manager.tasks, [])

    @patch("builtins.input", return_value="1")
    def test_delete_task(self, mock_input):
        task_manager.tasks.append("Study Python")
        task_manager.delete_task()
        self.assertEqual(task_manager.tasks, [])

    def test_add_multiple_tasks(self):
        task_manager.tasks.append("Task 1")
        task_manager.tasks.append("Task 2")
        self.assertEqual(len(task_manager.tasks), 2)


if __name__ == "__main__":
    unittest.main()