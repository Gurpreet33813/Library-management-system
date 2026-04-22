from utils import issued_books,books
#Return books
def Return_books():
    name = input("Enter the book name: ")
    if name in Issued_books():
        Issued_books.remove(name)
        books.append(name)
        print("Book returned")
    else:
