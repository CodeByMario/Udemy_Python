# importing the file library_function
import utility.library_function as lf

def add_book():
    lf.input_()
    lf.add_to_library()

def list_book():
    try:
        lf.load_data_base()
        lf.library_show()
    except:
        print("Empty")

def read_book():
    lf.input_()
    lf.mark_read()

def delete_book():
    lf.input_()
    for book in lf.library:
        if book['name'] == lf.name and book['author'] == lf.author:
            lf.library.remove(book)
            print("Book removed Successfully")
            break
        else:
            print(f"No book name {lf.name.title()} is in library!!")

def quit_program():
    print("Thank you! Visit again.")

USER_INPUT = """
ENTER:
- 'a' to add new Book
- 'l' to list all Books
- 'r' to mark a Book as read
- 'd' to delete a Book
- 'q' to quit
"""
user_input = ''
while user_input != 'q':
    user_input = input(USER_INPUT).lower()
    function = {
        'a': add_book,
        'l': list_book,
        'r': read_book,
        'd': delete_book,
        'q': quit_program
    }
    
    
    
    if user_input in function:
        function[user_input]()
        lf.save_data_base()
    else:
        print("Invalid input, please try again.")
