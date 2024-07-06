def get_todo_list():
  try:
    with open("todo.txt", "r") as file:
      todos = file.readlines()
      return [todo.strip() for todo in todos]
  except FileNotFoundError:
    return []

def save_todo_list(todos):

  with open("todo.txt", "w") as file:
    file.writelines(todos)

def print_todos(todos):
  if not todos:
    print("There are no tasks in your to-do list.")
    return
  for i, todo in enumerate(todos):
    print(f"{i+1}. {todo}")

def add_todo():
  new_todo = input("Enter a new to-do item: ")
  todos.append(new_todo)
  print(f"Task '{new_todo}' added to the list.")
  save_todo_list(todos)

def complete_todo():
  print_todos(todos)
  if not todos:
    return
  while True:
    try:
      index = int(input("Enter the number of the task to mark complete (or 0 to cancel): ")) - 1
      if 0 <= index < len(todos):
        completed_todo = todos.pop(index)
        print(f"Task '{completed_todo}' marked complete and removed from the list.")
        save_todo_list(todos)
        return
      elif index == -1:
        return  # Cancel marking complete
      else:
        print("Invalid input. Please enter a number between 0 and", len(todos))
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  global todos  # Make the list accessible within functions
  todos = get_todo_list()

  while True:
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task complete")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
      print_todos(todos)
    elif choice == "2":
      add_todo()
    elif choice == "3":
      complete_todo()
    elif choice == "4":
      print("Exiting the To-Do List application.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()
