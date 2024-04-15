# djanglers
# Group Members: Paul, Timny, Nick
# This one is made by Paul


class NotExactlyFiveCenturiesError(Exception):
    pass


def main():
    try:
        age = int(input("ENTER YOUR AGE: "))
        if age != 500:
            raise NotExactlyFiveCenturiesError("YOU ARE NOT WORTHY, CHILD!")
        else:
            print("YOU MAY SIP!")

    except ValueError:
        print("Dont try and trick me child. Enter a integer.")
        main()

    except NotExactlyFiveCenturiesError as e:
        print(f"NotExactlyFiveCenturiesError: {e}")


if __name__ == "__main__":
    main()
