#!/usr/bin/python3
"""
Fetches data from an API
and returns information about the employee's todo list progress
"""


import requests
import sys

def fetch_employee_todo_progress(employee_id):
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Fetch employee details
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        if user_response.status_code != 200:
            print("Employee not found")
            return

        employee = user_response.json()
        employee_name = employee.get("name")

        # Fetch TODO list for the employee
        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todos = todos_response.json()

        # Calculate completed and total tasks
        completed_tasks = [todo for todo in todos if todo.get("completed")]
        total_tasks = len(todos)
        done_tasks_count = len(completed_tasks)

        # Display the employee's TODO progress
        print(f"Employee {employee_name} is done with tasks({done_tasks_count}/{total_tasks}):")

        # Display the titles of completed tasks
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")


