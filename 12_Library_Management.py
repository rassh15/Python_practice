"""
Create a library class
having methods like
display book
lend a book
add a book
return a book
maintain dictionay with 
key value pair like books and name of person
object be like
nameLibrary = Library(listOfBooks, library_name)

create a main function with infinite loop asking user
for an input

"""
import collections

class Library:

    books_data = collections.defaultdict(list)


    def __init__(self, books, lib_name):
        self.ListOfBooks = books
        self.LibraryName = lib_name

    def displayBook(self):
        print(f"\nBooks Available in {self.LibraryName}\n")
        for i in self.ListOfBooks:
            print(i)

    def lendBook(self):
        print("Which Book do want to select: ")
        self.displayBook()

        print("Enter the name of the book: ", end='')
        book_choice = input()
        if book_choice in self.ListOfBooks:
            name = input("Enter your name: ")
            self.books_data[book_choice].append(name)
            self.ListOfBooks.remove(book_choice)
            print("Book Granted")


        else:
            for keys, values in self.books_data.items():
                if keys == book_choice:
                    print(f"{keys} is retain by {values}")
                else:
                    print(f"{book_choice} not availabe ")

    def addBook(self):
        self.ListOfBooks.append(input("Enter the name of the book: "))
        print("Book Successfully Accepted")

          

    def returnBook(self):
        user_name = input("Enter you name: ")
        book_name = input("Enter book name: ")

        self.ListOfBooks.append(book_name)

        self.books_data[book_name].remove(user_name)
        print("Book Returned Successfully! ")

if __name__ == '__main__':

    books = ["In Search of Lost Time","Ulysses",
    "Don Quixote","1One Hundred Years","The Great Gatsby","War & Peac"]
    rasshLib = Library(books, "Rashid's Library")

    print(f"Welcome to {rasshLib.LibraryName}")
    while True:

        print("\n1. Display Available Books\n2.Lend Book\n3. Add Book\n4. Return Book\n5. Exit")
        ch = input("Choose: ")
        if ch == "1":
            rasshLib.displayBook()

        elif ch == "2":
            rasshLib.lendBook()


        elif ch == "3":
            rasshLib.addBook()


        elif ch == "4":
            rasshLib.returnBook()
            
        elif ch == "5":
            break
        



    