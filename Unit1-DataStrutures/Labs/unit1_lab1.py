#Unit 1 - Lab 1: Exploring Python Dictionaries

def grade_summary(student_grades):
    '''Quick summary of all student grades'''

    print("\nSummary:\n---------------")
    #Total number of students
    print("Number of students:", len(student_grades))
    percent_grades = convert_grades(student_grades)
    #Highest grade
    print(f"Highest grade: {max(percent_grades.values())}%")
    #Lowest grade
    print(f"Lowest grade: {min(percent_grades.values())}%")
    #Average grade
    print(f"Average grade: {average_grade(percent_grades)}%")
    print()


def convert_grades(grades):
    '''Converts letter grades to numeric grades'''

    grade_numbers = {
        "A+": 99, "A": 95, "A-": 90,
        "B+": 89, "B": 85, "B-": 80,
        "C+": 79, "C": 75, "C-": 70,
        "D+": 69, "D": 65, "D-": 60,
        "F": 49
    }

    for student, grade in grades.items():
        if grade in grade_numbers:
            grades[student] = grade_numbers[grade]

    return grades


def average_grade(grades):
    '''Calculates average grade'''
    total = 0
    for grade in grades.values():
        total += grade
    return total/len(grades)


def main():
    #Create the dictionary
    student_grades = {
        "Stephen": 89,
        "Paul": 69,
        "Matt": "A",
        "Timny": "B",
        "Liam": 79,
        "Requis": "C+",
        "JFK": 82
        }
    
    #Update dictionary
    student_grades.update({"Nick" : "A+", "John" : 82, "Stephen" : 92})

    #Accessing Elements
    try:
        print("\nStephens grade:", student_grades["Stephen"])
        print(student_grades["Mohammad"])
    except KeyError:
        print("Error: The name Mohammad is not in the dictionary!")

    #Delete elements - del
    del student_grades["Liam"]
    #pop()
    print("\nRemoved grade:", student_grades.pop("Timny"))
    #popitem()
    s, g = student_grades.popitem()
    print(f"Removed student: {s}: {g}")

    #Looping - first loop
    print("\nStudent grades:\n---------------")
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")

    #Looping - Modified loop (Highest grades)
    print("\nHigh Grades:\n---------------")
    for student, grade in student_grades.items():
        if grade == "A":
            print(f"{student}: {grade}")
        elif type(grade) == int and grade > 90:
            print(f"{student}: {grade}%")

    #BONUS!
    grade_summary(student_grades)

main()