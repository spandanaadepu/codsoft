class TodoList:
    def __init__(self):
        self.tasks=[]

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def display_task(self):
        if self.tasks:
            print("TO-DO LIST")
            for index,task in enumerate(self.tasks,start=1):
                print(f"{index},{task}")
        else:
            print("List is empty")
            

    def update_task(self, index,new_task):
        if 1 <= index <= len(self.tasks):
            new_task=self.tasks[index-1]
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid tas0k number.")

def main():
    todo_list = TodoList()  
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Display Task")
        print("3. update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice:\n ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_task()
        elif choice == '3':
            index = int(input("Enter the index no you want to update: "))
            new_task=input("enter update task:")
            todo_list.update_task(index,new_task)
        elif choice == '4':
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
