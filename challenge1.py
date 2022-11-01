class Student:
    """A class to represent a University student."""
    # Add code here...
    def __init__(self, firstname, lastname, course):
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.module_list = []

    def show_details(self):
        print(self.firstname, self.lastname, "offering", self.course)
        if len(self.module_list) == 0:
            print("not enrolled")
        else:
            print("enrolled in the following modules")
            for m in self.module_list:
                print(m)

    def change_course(self, new_course):
        self.course = new_course

class Module:
    """A class to represent a single module."""
     # Add code here...
    def __init__(self, name, code, tutor):
        self.name = name
        self.code = code
        self.tutor = tutor
        self.module_student = []

    def enrol_student(self, student):
        self.module_student.append(student)
        student.module_list.append(self.code)

    def show_all_enrolled_students(self):
        for s in self.module_studentmodule_student:
            print(self.firstname, self.lastname)

def main():

    # Create some students and some modules...
    s1 = Student('Ken', 'Barlow', 'English')
    s2 = Student('Mike', 'Baldwin', 'Business')
    s3 = Student('Harold', 'Legg', 'Medicine')

    m1 = Module('English language and semantics', 'A101', 'Wanda Pickle')
    m2 = Module('Engineering principles', 'E102', 'Buzz Jones')
    m3 = Module('Anatomy', 'M105', 'Greg House')

    # Now enrol some students on some modules...
    m1.enrol_student(s1)
    m1.enrol_student(s2)
    m2.enrol_student(s1)
    m2.enrol_student(s3)

    # Have a look at some students and some modules...
    s1.show_details()
    s2.show_details()
    s3.show_details()

    m1.show_all_enrolled_students()
    m2.show_all_enrolled_students()
    m3.show_all_enrolled_students()

    # Change a course...
    s1.change_course('Engineering')
    s1.show_details()


if __name__ == "__main__":
    main()
