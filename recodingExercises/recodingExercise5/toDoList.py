def to_do_list():
    to_do = []
    action = ""
    while action != "1":
        action = int(input("What would you like to do:\n"
        "   to add task press 'a'\n"
        "   to view tasks press 'v'\n"
        "   to remove tasks press 'r'\n"
        "   to quit press '1': "))
        if action.lower() == 'a':
            add_task(to_do)
        elif action.lower() == 'v':
            view_task(to_do)
        elif action.lower() == 'n':
            remove_task(to_do)
        elif action != '1':
            print("\nInput a valid option\n")
        funcs[action-1](to_do)

    funcs=[add_task,view_task,remove_task]
    while action != "1":
        action = int(input("What would you like to do:\n"
        "   to add task press '1'\n"
        "   to view tasks press '2'\n"
        "   to remove tasks press '3'\n"
        "   to quit press '0': "))
        funcs[action-1](to_do)


def add_task(to_do):
    task = input("\nEnter your task: ").strip()
    if task == "":
        print("\nYou have not added any task\n")
    else:
        to_do.append(task)
        print("\nYour task has been added\n")

def view_task(to_do):
    if not to_do:
        print("\nYour to-do list is empty\n")
    else:
        print("\n")
        for num, task in enumerate(to_do):
            print(f"{num+1}. {task}")
        print("\n")

def remove_task(to_do):
    if not to_do:
        return "\nYour to-do list is empty\n"
    taskNo = int(input("\nEnter the no of the task to remove: "))
    to_do.pop(taskNo-1)
    print("Task removed...\n")

to_do_list()
print("Thanks for using this service")