# introspect.py
import json
import re

def extract_json_comment(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # Extract JSON comment from the file
        match = re.search(r'"""\s*({.*?})\s*"""', content, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        else:
            raise ValueError("No JSON comment found in the file.")

def display_all_fields(json_comment):
    print(json.dumps(json_comment, indent=4))

def display_specific_fields(json_comment):
    fields = list(json_comment.keys())
    print("Available fields to display:")
    for idx, field in enumerate(fields, start=1):
        print(f"{idx}. {field}")
    
    choices = input("Enter the numbers of the fields you want to display, separated by commas (e.g., 1,2): ")
    selected_fields = [fields[int(choice.strip())-1] for choice in choices.split(',')]
    
    selected_data = {field: json_comment[field] for field in selected_fields}
    print(json.dumps(selected_data, indent=4))

def main_menu(json_comment):
    while True:
        print("\nMenu:")
        print("1. Display all fields")
        print("2. Choose specific fields to display")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_all_fields(json_comment)
        elif choice == '2':
            display_specific_fields(json_comment)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    file_path = './sample_data/example.py'
    try:
        json_comment = extract_json_comment(file_path)
        main_menu(json_comment)
    except ValueError as e:
        print(e)

"""
Menu:
1. Display all fields
2. Choose specific fields to display
3. Exit
Enter your choice: 2
Available fields to display:
1. description
2. author
3. version
4. functions
Enter the numbers of the fields you want to display, separated by commas (e.g., 1,2): 1
{
    "description": "This module provides an example function."
}

Menu:
1. Display all fields
2. Choose specific fields to display
3. Exit
Enter your choice: 3
"""