# Added for day 2
class InvalidEditionError(Exception):
    pass


class Book:
    def __init__(self, title, author, edition=1):
        self.__title = title
        self.__author = author
        self.__edition = edition

    def get_info(self):
        return {"title": self.__title, "author": self.__author}

    @property
    def edition(self):
        return self.__edition

    # Added for day 2
    @edition.setter
    def edition(self, n):
        if n > 0:
            self.__edition = n
        else:
            raise InvalidEditionError("Edition number must be greater than 0")


def main():
    book = Book("Harry Potter", "J.K. Rowling", edition=2)

    # Ensuring that it cannot be accessed or changed
    book.__edition = 1  # Does nothing
    # print(book.__edition) raises an error

    # Catching a negative number (day 2)
    try:
        book.edition = -1
    except InvalidEditionError as e:
        print(f"Error: {e}")
    finally:
        book.edition = 1

    print(book.get_info())
    print(f"Edition: {book.edition}")


if __name__ == "__main__":
    main()
