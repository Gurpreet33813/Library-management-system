#show books
def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Books are available")
        for b in books:
            print(b)
