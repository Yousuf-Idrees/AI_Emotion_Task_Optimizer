# tasks.py
class Task:
    def __init__(self, name, priority, emotion_fit, category):
        self.name = name
        self.priority = priority
        self.emotion_fit = emotion_fit  # list of suitable emotions
        self.category = category

def get_user_tasks():
    tasks = []
    user_type = input("Are you:\n1. Student\n2. Employee\nChoice: ")
    
    if user_type == "1":
        print("\nEnter Academic Tasks (type 'done' to stop)")
        while True:
            name = input("Task name: ")
            if name.lower() == "done":
                break
            priority = int(input("Priority (1-5): "))
            tasks.append(Task(name, priority, ["neutral","happy","focused"], "academic"))

        print("\nEnter Personal / Life Activities (type 'done' to stop)")
        while True:
            name = input("Activity name: ")
            if name.lower() == "done":
                break
            tasks.append(Task(name, 3, ["neutral","happy","tired"], "life"))
    else:
        print("\nEnter Work Tasks (type 'done' to stop)")
        while True:
            name = input("Task name: ")
            if name.lower() == "done":
                break
            priority = int(input("Priority (1-5): "))
            tasks.append(Task(name, priority, ["neutral","happy","focused"], "work"))

        print("\nEnter Personal / Life Activities (type 'done' to stop)")
        while True:
            name = input("Activity name: ")
            if name.lower() == "done":
                break
            tasks.append(Task(name, 3, ["neutral","happy","tired"], "life"))
    
    print("\nEnter Break Activities (type 'done' to stop)")
    while True:
        name = input("Break activity: ")
        if name.lower() == "done":
            break
        tasks.append(Task(name, 2, ["sad","angry","tired"], "break"))
    
    return tasks
