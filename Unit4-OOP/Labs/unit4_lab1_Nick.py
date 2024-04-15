# Unit 4 Lab 1 - Senario 2 "The Overzealous Library"
# Group members: Nicholas Balsom, Timny Li, Paul Crocker
# Nick made this one


class NotEnoughBooksError(Exception):
    pass


def checkout_books(n):
    if n < 10:
        raise NotEnoughBooksError("CHECKOUT MORE BOOKS! MORE IS MORE!")
    else:
        print("Thank you for using our library. :)")


def main():
    try:
        checkout_books(int(input("How many books are you checking out: ")))
    except ValueError:
        print("NO, NO, Enter an Integer")
    except NotEnoughBooksError as e:
        print("NotEnoughBooksError:", e)


if __name__ == "__main__":
    main()
