# Python Introspect Utility

## Overview

This utility provides a way to add JSON-style comments in Python files and introspect them similarly to how Javadoc works in Java. The idea is to insert metadata in JSON format within the Python file and then use a Python script to read and display this metadata in an interactive manner.

## Files

1. **example.py**  
   This Python file contains the code along with JSON-style comments at the top, describing the module, author, version, and functions.

2. **introspect.py**  
   A script that reads and introspects the JSON-style comment in a Python file. It parses the JSON metadata and presents it interactively to the user.

## Features

- **JSON-style Comments**:  
  Allows you to add metadata (e.g., module description, author, version, function details) in a structured JSON format within Python comments.
  
- **Introspection**:  
  Extracts the JSON-style comment and presents it to the user in an interactive menu format, similar to Javadoc.
  
- **Interactive Menu**:  
  Provides a menu for the user to display all fields or select specific fields to view, making it easy to introspect the metadata.

## Example

### example.py
```python
# {
#   "module": "example",
#   "author": "John Doe",
#   "version": "1.0",
#   "description": "This is an example module to demonstrate introspection.",
#   "functions": [
#     {
#       "name": "example_function",
#       "description": "A sample function.",
#       "parameters": [
#         {"name": "name", "type": "str", "description": "The name to greet."}
#       ],
#       "return": "None"
#     }
#   ]
# }

def example_function(name: str) -> None:
    """
    Prints a greeting message.

    :param name: The name to greet.
    :type name: str
    :return: None
    """
    print(f"Hello, {name}!")

```

```
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
```

## Pros and Cons
### Pros:
Highly Customizable: Tailor the introspection process to fit specific metadata needs, including additional fields or custom formatting.
Interactive: Provides a dynamic, user-driven interface to inspect metadata, making it more engaging than static documentation.
Flexible: Easily extendable to handle more complex or varied metadata formats.
Cons:
Manual Maintenance: You have to keep the custom script updated for new features or changes to the metadata format.
Less Ecosystem Support: Unlike tools like Sphinx or Pdoc, it doesn’t have an extensive ecosystem of plugins or community support.
Requires Setup: You need to integrate it into your project manually and ensure the script is run appropriately.
Comparison to Established Tools

# Comparison to Established Tools

| Tool                       | Pros                                                   | Cons                                |
|----------------------------|--------------------------------------------------------|-------------------------------------|
| pydoc                      | Simple, built-in, no setup required                    | Limited customization               |
| Sphinx                     | Highly customizable, multiple output formats           | Steeper learning curve, requires setup |
| pdoc                       | Simple and easy to use, clean output                   | Less customizable than Sphinx       |
| Pycco                      | Generates literate-style documentation                 | Best for small projects             |
| Custom Script (introspect.py) | Highly customizable, interactive                       | Requires manual maintenance for json formatting (or tools to be extended)|



For simple documentation, tools like pydoc or pdoc are choices. For customized and interactive needs, the introspect.py script provides a flexible, tailored solution. For comprehensive and professional documentation, especially for large projects, Sphinx is the best choice.

You can use a hybrid approach: generate standard documentation with tools like Sphinx and supplement it with custom scripts like introspect.py for specific tasks.

Introspect.py can be extended with:

    1.Auto-document with Cross-referencing and Indexing.
    2.Version Control Integration (e.g. linking with git references)
    3.Search Functionality: In-built-in search functionality on both code and generated documentation.

