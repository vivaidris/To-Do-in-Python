import json
import csv
import os

os.makedirs('json_files', exist_ok=True)
os.makedirs('csv_files', exist_ok=True)
logged_in = False


def main_menu(username):
    print("Hello, " + username)
    while True:
        print('\nMain Menu:')
        print(' 1. Make a new list \n 2. View current lists \n 3. Delete a list \n 4. Settings \n 5. Logout')
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Enter the title of your new list")
            list_title = input()
            print("Enter the items in your list (comma-separated): ")
            items = input().split(',')
            list_data = {
                "title": list_title,
                "items": [item.strip() for item in items]
            }
            with open(f'csv_files/{list_title}.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Item', 'Done'])
                for item in list_data['items']:
                    writer.writerow([item, 'False'])
            print(f"List '{list_title}' created successfully.")

        elif choice == '2':
            seeing_lists = True
            while seeing_lists:
                print("\nCurrent lists:")
                csv_files = [f[:-4] for f in os.listdir('csv_files') if f.endswith('.csv')]

                if not csv_files:
                    print("No lists available.")
                    break
                else:
                    for file in csv_files:
                        print(f"- {file}")

                    print("Which file would you like to select? (Enter the name without .csv or 'exit' to leave)")
                    selected_file = input("> ").strip()

                    if selected_file.lower() == 'exit':
                        seeing_lists = False
                        break
                    elif selected_file in csv_files:
                        task_Menu = True
                        while task_Menu:
                            file_path = f'csv_files/{selected_file}.csv'
                            with open(file_path, 'r') as csvfile:
                                reader = csv.reader(csvfile)
                                header = next(reader, None)
                                rows = list(reader)

                            fixed_rows = []
                            for row in rows:
                                if len(row) == 1:
                                    fixed_rows.append([row[0], 'False'])
                                elif len(row) == 2:
                                    fixed_rows.append(row)

                            with open(file_path, 'w', newline='') as csvfile:
                                writer = csv.writer(csvfile)
                                writer.writerow(['Item', 'Done'])
                                writer.writerows(fixed_rows)
                            tasks = fixed_rows

                            print(f"\nFile: {selected_file}")
                            if not tasks:
                                print("No tasks found in this list.")
                            else:
                                for i, row in enumerate(tasks, start=1):
                                    if len(row) == 2:
                                        task, done = row
                                        status = "[X]" if done == 'True' else "[ ]"
                                        print(f"{i}. {status} {task}")
                                    else:
                                        print(f"{i}. Invalid task format: {row}")

                            print("\nOptions:")
                            print("1. Add a new task")
                            print("2. Edit a task")
                            print("3. Delete a task")
                            print("4. Toggle task completion")
                            print("5. Go back to list selection")
                            task_choice = input("> ").strip()

                            if task_choice == '1':
                                print("Enter the new task:")
                                new_task = input("> ").strip()
                                if new_task:
                                    with open(file_path, 'a', newline='') as csvfile:
                                        writer = csv.writer(csvfile)
                                        writer.writerow([new_task, 'False'])
                                    print("Added task!")
                                else:
                                    print("Task cannot be empty.")

                            elif task_choice == '2':
                                if not tasks:
                                    print("No tasks to edit.")
                                    continue
                                print("Enter the number of the task you want to edit:")
                                try:
                                    index = int(input("> ")) - 1
                                    if 0 <= index < len(tasks):
                                        print(f"Current task: {tasks[index][0]}")
                                        print("Enter the new task description:")
                                        new_desc = input("> ").strip()
                                        if new_desc:
                                            tasks[index][0] = new_desc
                                            with open(file_path, 'w', newline='') as csvfile:
                                                writer = csv.writer(csvfile)
                                                writer.writerow(['Item', 'Done'])
                                                writer.writerows(tasks)
                                            print("Task updated.")
                                        else:
                                            print("Task cannot be empty.")
                                    else:
                                        print("Invalid number.")
                                except ValueError:
                                    print("Invalid input.")

                            elif task_choice == '3':
                                if not tasks:
                                    print("No tasks to delete.")
                                    continue
                                print("Enter the number of the task to delete:")
                                try:
                                    index = int(input("> ")) - 1
                                    if 0 <= index < len(tasks):
                                        print(f"Are you sure you want to delete '{tasks[index][0]}'? (y/n)")
                                        confirm = input("> ").strip().lower()
                                        if confirm == 'y':
                                            removed = tasks.pop(index)
                                            with open(file_path, 'w', newline='') as csvfile:
                                                writer = csv.writer(csvfile)
                                                writer.writerow(['Item', 'Done'])
                                                writer.writerows(tasks)
                                            print(f"Deleted '{removed[0]}'.")
                                        else:
                                            print("Cancelled.")
                                    else:
                                        print("Invalid number.")
                                except ValueError:
                                    print("Invalid input.")

                            elif task_choice == '4':
                                if not tasks:
                                    print("No tasks to toggle.")
                                    continue
                                print("Enter the number of the task to toggle completion:")
                                try:
                                    index = int(input("> ")) - 1
                                    if 0 <= index < len(tasks):
                                        tasks[index][1] = 'False' if tasks[index][1] == 'True' else 'True'
                                        with open(file_path, 'w', newline='') as csvfile:
                                            writer = csv.writer(csvfile)
                                            writer.writerow(['Item', 'Done'])
                                            writer.writerows(tasks)
                                        print(f"Marked '{tasks[index][0]}' as {'complete' if tasks[index][1] == 'True' else 'incomplete'}.")
                                    else:
                                        print("Invalid number.")
                                except ValueError:
                                    print("Invalid input.")

                            elif task_choice == '5':
                                task_Menu = False
                            else:
                                print("Invalid option.")
                    else:
                        print("Invalid selection. Please try again.")

        elif choice == '3':
            print("Lists:")
            csv_files = [f for f in os.listdir('csv_files') if f.endswith('.csv')]
            if not csv_files:
                print("No lists to delete.")
                continue
            for i, file in enumerate(csv_files, 1):
                print(f"{i}. {file[:-4]}")
            print("Enter the number of the list you want to delete (or 'exit' to exit):")
            selection = input("> ").strip()
            if selection.lower() == 'exit':
                continue
            try:
                index = int(selection) - 1
                if 0 <= index < len(csv_files):
                    file_to_delete = csv_files[index]
                    print(f"Are you sure you want to delete '{file_to_delete[:-4]}'? (y/n)")
                    confirm = input("> ").strip().lower()
                    if confirm == 'y':
                        os.remove(f'csv_files/{file_to_delete}')
                        print(f"List '{file_to_delete[:-4]}' deleted successfully.")
                    else:
                        print("Deletion cancelled.")
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Settings are not implemented yet.")

        elif choice == '5':
            print("You have been logged out.")
            break

        else:
            print("Invalid option. Try again.")


# Login/Signup System
print("Hello user!\n")
print("Would you like to sign up or login? (Enter 'signup' or 'login')")
input_a = input()

if input_a == "signup":
    print("Enter your username:")
    username = input()
    print("Enter your password:")
    password = input()

    user_data = {
        "username": username,
        "password": password
    }

    print("Are you sure (y/n)?")
    confirm = input()
    if confirm.lower() == 'y':
        with open('json_files/users.json', 'w') as file:
            json.dump(user_data, file, indent=4)
        logged_in = True
        main_menu(username)
    else:
        print("Signup cancelled.")
        exit()

elif input_a == "login":
    print("Enter your username: ")
    username = input()
    print("Enter your password: ")
    password = input()

    with open('json_files/users.json', 'r') as file:
        users = json.load(file)

    if username == users.get("username") and password == users.get("password"):
        logged_in = True
        main_menu(username)
    else:
        print("Login failed. Please check your username and password.")

