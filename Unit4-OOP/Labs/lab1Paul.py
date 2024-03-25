# djanglers
# Group Members: Paul, Timny, Nick
# Paul made this one
import itertools as iter
import sys

sys.setrecursionlimit(1000000000)


class NotExactlyFiveCenturiesError(Exception):  # this is a class
    pass


try:
    if int(input("Input your age (there is so specific age): ")) == 500:  # this does stuff
        print("Enjoy your drink")
    else:
        raise NotExactlyFiveCenturiesError("ahiduhsa")

except ValueError:
    asdijadoa = "Please enter a valid input"
    asdijadoa_2 = list(iter.chain.from_iterable(asdijadoa))  # adad'asda] stuff about stuff
    print(asdijadoa_2)

except NotExactlyFiveCenturiesError:
    age_response = "You are NOT the right age..."

    def function1():  # if its wrong
        for temporary_variable in age_response.split():
            print(temporary_variable)
        function1()

    function1()
