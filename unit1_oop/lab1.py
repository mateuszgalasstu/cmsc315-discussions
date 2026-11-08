class Person:
    """
    Parent class representing a person with a name and age.
    """
    def __init__(self, name: str, age: int):
        # TODO: Initialize name and age instance variables
        self.name = name
        self.age = age

    def display_info(self):
        """Print the person's name and age in the specified format."""
        # TODO: Implement method to print name and age
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    """
    Child class representing a student, inherits from Person.
    Adds student_id, courses list, and school_name class variable.
    """
    school_name = "Generic University"

    def __init__(self, name: str, age: int, student_id: str):
        # TODO: Call parent constructor and initialize student_id and courses list
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []




    def enroll_course(self, course_name: str):
        """Enroll the student in a new course by adding to the courses list."""
        # TODO: Add course_name to the courses list
        self.courses.append(course_name)

    def display_info(self):
        """
        Print the student's name, age, student ID, school name, and list of courses in the specified format.
        """
        # TODO: Implement method to print all student details, including courses
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, School: {self.school_name}, Courses: [{', '.join(self.courses)}]")

# --- Demonstration code ---
if __name__ == "__main__":
    # Creating and displaying a Person
    # TODO: Create a Person and call display_info
    person1 = Person("Laura", 23)
    person1.display_info()


    # Creating and displaying a Student
    # TODO: Create a Student, enroll in courses, and call display_info
    student1 = Student("Mateusz", 23, "313432")
    student1.enroll_course("Object Oriented Programming")
    student1.enroll_course("Networking 101")
    student1.display_info()

    # Changing the class variable
    # TODO: Change school_name and show it affects all Student instances
    Student.school_name = "Harvard"
    student2 = Student("John", 25, "315321")
    student2.enroll_course("Java 101")
    student2.display_info()
    student1.display_info()
