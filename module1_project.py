# Module 1 Project - To Do Application |
#---------------------------------------

def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit Application")
    
        choice = input("Enter your choice: ")
    
        if choice =='1':
            try:
                n_tasks = int(input("How many tasks would you like to add: "))
                if n_tasks <1:
                    print("Please enter a positive number greater than zero.")
                    continue
            except ValueError:
                print("Invlaid input. Please enter a valid number.")
                continue
        
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append(task)
                print("Task added!")
            
        elif choice == '2':
            if len(tasks) == 0:
                print("There are currently no tasks on your to-do list. Great work!")
            else:
                print("\nTasks:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")
            
        elif choice == '3':
            try:
                task_index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    del tasks[task_index]
                    print(f"{task_index + 1} has been deleted.")
                else:
                    print("Invalid selection.")
            except ValueError:
                    print("Please enter a valid number.")
        elif choice == '4':
            print("Thank you for using the to-do list app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()