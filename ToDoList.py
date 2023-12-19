class FileHandler:
    def __init__(self):
        pass

    def write_entry(self, todo, due_date):
        with open ("ToDo.txt", "a") as f:
            f.write(f"{todo};{due_date}\n")


class Entry:
    def __init__(self):
        self.todo = ""
        self.due_date = ""
        self.todolist = FileHandler()

    def add_todo(self, todo, due_date):
        self.todo = todo
        self.due_date = due_date
        self.todolist.write_entry(todo, due_date)


class ToDoListApplication:
    def __init__(self):
        self.todo = Entry()

    def add_entry(self, todo, due_date):
        self.todo.add_todo(todo, due_date)    

    def help(self):
        print("Commands:")
        print("0 - exit")
        print("1 - add ToDo")
        print("2 - show all ToDos")
        print("3 - mark ToDo as Done")
        print("4 - clear all ToDos")

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                print("exiting ToDoList")
                break
            elif command == "1":
                todo = input("Please input a ToDo: ")
                due_date = input("Due date: ")
                self.add_entry(todo, due_date)
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "4":
                pass   

if __name__ == "__main__":
    todolist = ToDoListApplication()
    todolist.execute()
