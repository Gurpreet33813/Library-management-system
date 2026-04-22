from add import add_books
from show import show_books
from issue import issue_books
from return import return_books
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
