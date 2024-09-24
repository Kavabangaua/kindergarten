from collections import deque

#Модель даних
class Child:
    def __init__(self, name, birth_date, parent_name, application_date):
        self.name = name
        self.birth_date = birth_date
        self.parent_name = parent_name
        self.application_date = application_date

    def __str__(self):
        return f"Child: {self.name}, Born: {self.birth_date}, Parent: {self.parent_name}, Application Date: {self.application_date}"

#Модeль черги
class QueueManager:
    def __init__(self):
        self.queue = deque()

    def add_to_queue(self, child):
        if not isinstance(child, Child):
            raise TypeError("Object must be an instance of Child class")
        self.queue.append(child)

    def remove_from_queue(self):
        if self.queue:
            return self.queue.popleft()
        else:
            raise IndexError("Queue is empty")

    def view_queue(self):
        return list(self.queue)

#Інтерфейс користувача
def display_menu():
    print("\n1. Add Child to Queue")
    print("2. Remove Child from Queue")
    print("3. View Queue")
    print("4. Exit")

def get_child_info():
    name = input("Enter child's name: ")
    birth_date = input("Enter child's birth date (YYYY-MM-DD): ")
    parent_name = input("Enter parent's name: ")
    application_date = input("Enter application date (YYYY-MM-DD): ")
    return Child(name, birth_date, parent_name, application_date)

#Основна програма
def main():
    queue_manager = QueueManager()
    
    while True:
        display_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            child = get_child_info()
            queue_manager.add_to_queue(child)
        elif choice == '2':
            queue_manager.remove_from_queue()
        elif choice == '3':
            queue_manager.view_queue()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()