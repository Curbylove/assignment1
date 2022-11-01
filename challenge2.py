class Borrower:
    """Represents a person who can borrow books."""

    new_id_code = 1  # Class variable

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = Borrower.new_id_code
        Borrower.new_id_code += 1  # Updates for next new borrower...
        self.books_borrowed = []


class Book:
    """A class to represent a book in a library."""


class Library:
    """A class to represent a lending library."""


def main():
    # Create some books...
    book1 = Book('Kafkas Motorbike', 'Bridget Jones', 1290)
    book2 = Book('Cooking with Custard', 'Jello Biafra', 1002)
    book3 = Book('History of Bagpipes', 'John Cairncross', 987)

    # Put the books in the library
    library = Library()  # Creates the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create some borrowers...
    bor1 = Borrower('Kevin', 'Wilson')
    bor2 = Borrower('Rita', 'Shapiro')
    bor3 = Borrower('Max', 'Normal')

    library.add_borrower(bor1)
    library.add_borrower(bor2)
    library.add_borrower(bor3)

    # Make some loans...
    library.lend_book(bor1, book1)
    bor1.show_borrower_details()
    bor1.show_all_books()
    library.lend_book(bor2, book3)
    bor2.show_borrower_details()
    bor2.show_all_books()
    # Try to lend book3 out again...
    library.lend_book(bor3, book3)

if __name__ == "__main__":
        main()
