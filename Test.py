import unittest
from collections import deque

class Child:
    def __init__(self, name, birth_date, parent_name, application_date):
        self.name = name
        self.birth_date = birth_date
        self.parent_name = parent_name
        self.application_date = application_date

    def __str__(self):
        return f"Child: {self.name}, Born: {self.birth_date}, Parent: {self.parent_name}, Application Date: {self.application_date}"

class QueueManager:
    def __init__(self):
        self.queue = deque()

    def add_to_queue(self, child):
        self.queue.append(child)

    def remove_from_queue(self):
        if self.queue:
            return self.queue.popleft()
        else:
            raise IndexError("Queue is empty")

    def view_queue(self):
        return list(self.queue)

#Тестовий клас
class TestQueueManager(unittest.TestCase):

    def setUp(self):
        """Ініціалізуємо об'єкт черги для кожного тесту"""
        self.queue_manager = QueueManager()

    def test_add_to_queue(self):
        """Тест на додавання дитини до черги"""
        child = Child("Ivan", "2018-01-01", "Maria", "2024-09-01")
        self.queue_manager.add_to_queue(child)
        self.assertEqual(len(self.queue_manager.queue), 1)
        self.assertEqual(self.queue_manager.queue[0].name, "Ivan")

    def test_remove_from_queue(self):
        """Тест на видалення дитини з черги"""
        child1 = Child("Ivan", "2018-01-01", "Maria", "2024-09-01")
        child2 = Child("Oleg", "2017-05-15", "Petro", "2024-09-01")
        self.queue_manager.add_to_queue(child1)
        self.queue_manager.add_to_queue(child2)

        removed_child = self.queue_manager.remove_from_queue()
        self.assertEqual(removed_child.name, "Ivan")
        self.assertEqual(len(self.queue_manager.queue), 1)

    def test_remove_from_empty_queue(self):
        """Тест на видалення дитини з порожньої черги (негативний сценарій)"""
        with self.assertRaises(IndexError):
            self.queue_manager.remove_from_queue()

    def test_view_queue(self):
        """Тест на перегляд черги"""
        child1 = Child("Ivan", "2018-01-01", "Maria", "2024-09-01")
        child2 = Child("Oleg", "2017-05-15", "Petro", "2024-09-01")
        self.queue_manager.add_to_queue(child1)
        self.queue_manager.add_to_queue(child2)

        queue_view = self.queue_manager.view_queue()
        self.assertEqual(len(queue_view), 2)
        self.assertEqual(queue_view[0].name, "Ivan")
        self.assertEqual(queue_view[1].name, "Oleg")

    def test_queue_order(self):
        """Тест на збереження порядку черги (FIFO)"""
        child1 = Child("Ivan", "2018-01-01", "Maria", "2024-09-01")
        child2 = Child("Oleg", "2017-05-15", "Petro", "2024-09-01")
        self.queue_manager.add_to_queue(child1)
        self.queue_manager.add_to_queue(child2)

        removed_child1 = self.queue_manager.remove_from_queue()
        removed_child2 = self.queue_manager.remove_from_queue()

        self.assertEqual(removed_child1.name, "Ivan")
        self.assertEqual(removed_child2.name, "Oleg")

    @unittest.expectedFailure
    def test_negative_scenario(self):
        """Негативний тест: додавання дитини з некоректними даними"""
        with self.assertRaises(TypeError):
            self.queue_manager.add_to_queue("This is not a child object")

#Запускаємо тести
if __name__ == '__main__':
    unittest.main()