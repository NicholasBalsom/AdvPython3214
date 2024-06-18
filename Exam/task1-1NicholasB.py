# Task 1-1: Dictonaries and Recursion


def find_top_student(student_marks: dict):
    averages = []
    for marks in student_marks.values():
        sum = 0
        for mark in marks:
            sum += mark
        average = sum // len(marks)
        averages.append(average)

    index = averages.index(max(averages))
    top_student = list(student_marks.keys())[index]
    return top_student


def main():
    student_marks = {
        "Alice": [80, 90, 88],
        "Bob": [90, 92, 87],
        "Paul": [49, 26, 78],
        "Nick": [99, 100, 95],
        "dupe": [99, 100, 95],
    }

    top_student = find_top_student(student_marks)
    print(f"The top student is {top_student}")


if __name__ == "__main__":
    main()
