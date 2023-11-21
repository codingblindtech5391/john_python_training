
### To-Do List Project

**Project Overview:**
Create a command-line To-Do List application that allows users to add tasks, view tasks, mark tasks as completed, and remove tasks.

**Requirements:**

1. **Task Representation:**
   - Each task should have a unique identifier.
   - Store tasks in a data structure (e.g., list, dictionary).

2. **Functionality:**
   - **Add Task:** Allow the user to add tasks to the To-Do List.
   - **View Tasks:** Display all tasks in the To-Do List.
   - **Mark Task as Completed:** Provide an option to mark a task as completed.
   - **Remove Task:** Allow the user to remove a task from the list.

3. **User Interface:**
   - Create a simple command-line interface for interacting with the To-Do List.
   - Display a menu with options for adding, viewing, marking, and removing tasks.
   - Continuously prompt the user for input until they choose to exit.

4. **Persistence (Optional):**
   - Save the To-Do List to a file so that tasks persist between sessions.
   - Load the To-Do List from the file when the program starts.

**Implementation Steps:**

1. **Initialize the To-Do List:**
   - Create a data structure to store tasks (e.g., a list or dictionary).
   - If you choose to implement persistence, load existing tasks from a file.

2. **Display Menu:**
   - Show a menu with options for adding, viewing, marking, and removing tasks.
   - Include an option to exit the program.

3. **Add Task:**
   - Prompt the user to enter a task.
   - Assign a unique identifier to the task.
   - Add the task to the To-Do List.

4. **View Tasks:**
   - Display all tasks in a readable format.
   - Include information such as the task ID, description, and completion status.

5. **Mark Task as Completed:**
   - Ask the user for the task ID they want to mark as completed.
   - Update the task's completion status.

6. **Remove Task:**
   - Ask the user for the task ID they want to remove.
   - Remove the task from the To-Do List.

7. **Persistence (Optional):**
   - Save the To-Do List to a file whenever a change occurs.
   - Load the To-Do List from the file when the program starts.

8. **Repeat:**
   - After each operation, return to the main menu and continue until the user chooses to exit.

**Tips:**
- Encourage modular coding by breaking down functionality into functions (e.g., `add_task()`, `view_tasks()`, etc.).
- Use appropriate data structures and control flow statements.
- Test your program with various scenarios to ensure it handles different cases.

