class FileHandler:
    def __init__(self):
        pass

class ToDoList:
    def __init__(self):
        self.todolist = []



class Entry:
    def __init__(self):
        pass

class ToDoListApplication:
    def __init__(self):
        self.todo = ToDoList()

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
                pass
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "4":
                pass     