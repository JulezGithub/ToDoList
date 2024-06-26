class FileHandler:
    def __init__(self):
        pass

    def write_entry(self, todo, due_date):
        with open ("ToDo.txt", "a") as f:
            f.write(f"{todo};{due_date}\n")

    def read(self):
        with open ("ToDo.txt") as f:
            print(f"{"ToDo:":<20}{"Due Date":<10}")
            for line in f:
                line = line.strip()
                parts = line.split(";")
                todo = parts[0]
                due_date = parts[1]
                print(f"{todo:<20}{due_date:<20}")    

    def mark_done(self, done):
        all_entries = []
        with open ("ToDo.txt") as f:
            for line in f:
                parts = line.split(";")
                all_entries.append([parts[0], parts[1].strip()])
        for entry in all_entries:
            if done in entry:
                all_entries.remove(entry)
                print(all_entries)
        with open("ToDo.txt", "w") as f:
            pass
        for entry in all_entries:
            self.write_entry(entry[0], entry[1]) 

    def clear(self):
        with open("ToDo.txt", "w") as f:
            pass



class ToDoListApplication:
    def __init__(self):
        self.todo = FileHandler()

    def add_entry(self, todo, due_date):
        self.todo.write_entry(todo, due_date)    

    def show_entries(self):
        self.todo.read()

    def mark_done(self):
        done = input("What ToDo is done?: ")
        self.todo.mark_done(done)
    def clear(self):
        self.todo.clear()
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
                print("exiting ToDoList...")
                break
            elif command == "1":
                todo = input("Please input a ToDo: ")
                due_date = input("Due date: ")
                self.add_entry(todo, due_date)
            elif command == "2":
                self.show_entries()
            elif command == "3":
                self.mark_done()
            elif command == "4":
                self.clear()

if __name__ == "__main__":
    todolist = ToDoListApplication()
    todolist.execute()
    print("changed")
