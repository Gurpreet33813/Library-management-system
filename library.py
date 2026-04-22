#LIBRARY.PY

books = []
Issued_books = []

#Add books
def add_books():
    name = input("Enter the books name: ")
    books.append(name)
    print("books are added")
#show books
def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Books are available")
        for b in books:
            print(b)
#Issue
def Issue_books():
    name = input("Enter the book name: ")
    if name in books:
        books.remove(name)
        Issued_books.append(name)
        print("Books Issued")
    else:
        print("Book not available")
#Return books
def Return_books():
    name = input("Enter the book name: ")
    if name in Issued_books():
        Issued_books.remove(name)
        books.append(name)
        print("Book returned")
    else:
        print("Book not issued")
    
    


#!MAIN BODY
def library():
    while True:
        print("1.\nAdd books")
        print("2.show books")
        print("3.Issue books")
        print("4.Return books")
        print("5.exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            Issue_books()
        elif choice == 4:
            Return_books()
        elif choice == 5:
            print("Thank You")
        else:
            print("Invalid choice")
library()
