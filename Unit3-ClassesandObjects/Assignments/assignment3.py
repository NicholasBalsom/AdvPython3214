# Unit 3 Assignment
class Student:
    def __init__(self, name: str, age: int, student_id: str):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.__gpa = 0.0

    # Set gpa if greater than or equal to 0 and less than or equal to 4.0
    def set_gpa(self, gpa: float):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa

    # Returns the gpa (private)
    def get_gpa(self):
        return self.__gpa

    def study(self, hours: float):
        # If the students gpa would be grater than 4.0 after studying, gpa = 4.0
        if self.__gpa + (hours / 10) <= 4.0:
            self.__gpa += hours / 10
        else:
            self.__gpa = 4.0

    def display_student_info(self):
        print(
            f"Name: {self.name}\n"
            f" Age: {self.age}\n"
            f" Student id: {self.student_id}\n"
            f" GPA: {self.get_gpa():.1f}\n"
        )


# Create instances
nick = Student("Nicholas", 17, "nbalsom")
paul = Student("Paul", 17, "pcrocker")
timny = Student("Timny", 17, "tli")

# Using methods
nick.set_gpa(4.0)
paul.set_gpa(3.5)
timny.set_gpa(3.0)

nick.study(2.0)
paul.study(2.5)
timny.study(5.0)

# Display information
nick.display_student_info()
paul.display_student_info()
timny.display_student_info()
