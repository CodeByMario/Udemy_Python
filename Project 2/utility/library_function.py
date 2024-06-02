import json

author = "nan"
name = "nan"
library = []

# Input function to get input for Book_name and Book_Author_Name
def input_():
    global name, author
    name = input("Enter Book_Name: ")
    author = input("Enter Author_Name: ")

def add_to_library():
    global library
    book = {
        'name': name,
        'author': author,
        'read': False
    }
    library.append(book)

def library_show():
    print(f"|\t Book_Name \t|\t Author_Name \t|\t Read \t|")
    for book in library:
        print(f"|\t {book['name'].title()} \t|\t {book['author'].title()} \t|\t {book['read']} \t|")
    print("\t\t\t===X===\t\t\t")

def mark_read():
    global library
    for book in library:
        if book['name'] == name and book['author'] == author:
            book['read'] = True
    
def load_data_base():
    global library
    with open("library_data_base.json", "r") as file:
        library = json.load(file)

def save_data_base():
    with open("library_data_base.json", "w") as file:
        json.dump(library, file)


def validate():
    for book in library:
        if book['name'] == name:
            validate = True