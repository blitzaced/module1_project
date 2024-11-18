To-Do List Application v1.0

  The goal of this project was to create an application to help someone manage a simple to-do list.
  
  The features of the application are as follows:
  
    "Add Task"           - by selecting this menu option, the user may add a single task, or even multiple tasks to their list.
    "View Tasks"         - by selecting this menu option, the user may view all tasks currently present on their list, reflecting all changes made up to that point.
    "Delete Task"        - by selecting this menu option, the user may delete a single item from their current to-do list.
    "Quit Application"   - by selecting this menu option, the user may terminate the program when they are ready.

  
  The application will produce the following errors when applicable:
  
    Main Menu error:
      When asked to make a selection from the main menu, the application is expecting to receive an input value of 1-4.
        If any other value, integer/non-integer, is entered aside from values 1-4 the following error will show to the user:
          "Invalid choice. Please try again."
    ----------------------------------------------------------------------------------------------------------------------------------
    "Add Task" errors:
      When asked, "How many tasks would you like to add: ", the application is expected an integer >= 1. 
        If zero, or a negative integer are entered, the following error will show to the user:
          "Please enter a positive number greater than zero."
        If a non-integer character is entered (string/letter), the following error will show to the user:
          "Invalid input. Please enter a valid number."
    ----------------------------------------------------------------------------------------------------------------------------------
    "View Task" error:
      When the user asks to view their to-do when no tasks are present, the following error will show:
        "There are currently no tasks on your to-do list. Great work!"
    ----------------------------------------------------------------------------------------------------------------------------------
    "Delete Task" errors:
      When asked, "Enter the task number to delete: ", the application is expecting a task number currently present on the to-do list.
        If the number provided by the user does not correspond to a task number on the active list, the following error will show:
          "Invalid selection."
        If a non-integer character is entered (string/letter), the following error will show to the user:
          "Please enter a valid number."
      
      
