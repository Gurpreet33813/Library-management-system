from utils import books,issued_books
#Issue
def Issue_books():
    name = input("Enter the book name: ")
    if name in books:
        books.remove(name)
        Issued_books.append(name)
        print("Books Issued")
    else:
        print("Book not available")
