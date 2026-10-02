# Python Task Manager

A simple command-line task management application built with Python.

## Features

- Add tasks
- View tasks
- Complete tasks
- Delete tasks
- Input validation
- Error handling
- Unit testing
- Documentation

## Requirements

- Python 3.8 or higher
- No external packages are required

## Project Structure

```text
python-task-manager/
├── README.md
├── requirements.txt
├── main.py
├── task_manager.py
├── validation.py
├── errors.py
└── test_task_manager.py
Setup

Clone the repository:
git clone https://github.com/manasareddym077/python-task-manager.git
Open the project:
cd python-task-manager
Run the application:

python main.py
Run Tests

python -m unittest test_task_manager.py
How to Use

Choose an option from the menu:
Add Task
View Tasks
Complete Task
Delete Task
Exit
Validation
The application checks:
Empty task titles
Task titles longer than 100 characters
Invalid task IDs
Non-existing task IDs
Error Handling
The application uses custom errors and exception handling to safely handle invalid input and missing tasks.
Testing
Unit tests are included for:

Adding tasks
Validation
Completing tasks
Deleting tasks
Invalid task IDs
Missing tasks