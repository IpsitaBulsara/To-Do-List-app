from functions import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

# import functions
while True:
    user_action = input("Type add, show, edit, complete or exit:").strip()
    if user_action.startswith('add') :
            todo = user_action[4:] + "\n"
            # todos = functions.get_todos()
            todos = get_todos()
            todos.append(todo)

            write_todos(todos)
    elif user_action.startswith('show'):
            todos = get_todos()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1
            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number-1)
            write_todos(todos)
            print(f"Todo '{todo_to_remove}' was removed from the list.")
        except IndexError:
            print("There is no Item with that number.")
            continue

    elif user_action.startswith('exit'):
            break
    else:
        print("Command is not valid.")
print("Bye!")

