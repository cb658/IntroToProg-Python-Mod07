# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   BChristopherson, 03-JUN-2025, Updated Script
# ------------------------------------------------------------------------------------------ #
import json

# DATA -------------------------------------------- #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str  # Hold the choice made by the user.
students: list = []  # a table of student data


# TODO Create a Person Class (Done)
class Person:
    """
    This class holds information regarding a person's name

    Properties:
    student_first_name (string), the student's first name
    student_first_name (string), the student's last name

    Change Log: (Who, When, What)
    BChristopherson, 03-JUN-2025, Created Class
    """
    # TODO Add first_name and last_name properties to the constructor (Done)

    def __init__(self, student_first_name: str = "", student_last_name: str = ""):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

    # TODO Create a getter and setter for the first_name property (Done)
    @property
    def student_first_name(self):
        return self.__student_first_name.title()

    @student_first_name.setter
    def student_first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__student_first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    # TODO Create a getter and setter for the last_name property (Done)
    @property
    def student_last_name(self):
        return self.__student_last_name.title()

    @student_last_name.setter
    def student_last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__student_last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO Override the __str__() method to return Person data (Done)
    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name}'

# TODO Create a Student class the inherits from the Person class (Done)
class Student(Person):
    """
    This class holds information regarding a student's name and course enrollment

    Properties:
    student_first_name (string), the student's first name
    student_first_name (string), the student's last name
    course_name (string), the name of the course

    Change Log: (Who, When, What)
    BChristopherson, 03-JUN-2025, Created Class
    """
    # TODO call to the Person constructor and pass it the first_name and last_name data (Done)
    def __init__(self, student_first_name: str = "", student_last_name: str = "", course_name: str = ""):
        super().__init__(student_first_name = student_first_name, student_last_name = student_last_name)
        self.course_name = course_name

    # TODO add a assignment to the course_name property using the course_name parameter
    # TODO add the getter for course_name (Done)
    @property
    def course_name(self):
        return self.__course_name.title()

    # TODO add the setter for course_name (Done)
    @course_name.setter
    def course_name(self, value: str):
        self.__course_name = value

    # TODO Override the __str__() method to return the Student data (Done)
    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name},{self.course_name}'


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    BChristopherson, 03-JUN-2O25, Updated class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        BChristopherson, 03-JUN-2025, Updated function

        :param file_name: string data with name of file to read from
        :param student_data: list of student enrollments

        :return: list
        """
        try:
            file = open(file_name, "r")
            ###student_data = []
            json_students = json.load(file)
            file.close()

            ###student_objects = []
            for student in json_students:
                student: Student = Student(student_first_name=student["FirstName"],
                                                  student_last_name=student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student)

            ### remove file.close()

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file and not file.closed:
                file.close()

        ###return student_objects
            return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        BChristopherson, 03-JUN-2025, Updated function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            # TODO Add code to convert Student objects into dictionaries (Done)
            json_students: list =[]
            for student in student_data:
                student_json: dict \
                    = {"FirstName": student.student_first_name,
                       "LastName": student.student_last_name,
                       "CourseName": student.course_name}
                json_students.append(student_json)

            file = open(file_name, "w")
            json.dump(json_students, file, indent=2)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    BChristopherson, 03-JUN-2025, Updated class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        BChristopherson, 03-JUN-2025, Updated function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        BChristopherson, 03-JUN-2025, Updated function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        BChristopherson, 03-JUN-2025, Updated function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        BChristopherson, 03-JUN-2025, Updated function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        ###message:str = ""
        ###student_objects = []
        print("-" * 50)
        for student in student_data:
          #//TODO Add code to access Student object data instead of dictionary data
            ###print(f'Student {student["FirstName"]} '
                  ###f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print(f'Student {student.student_first_name} {student.student_last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        BChristopherson, 03-JUN-2025, Updated function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")

            #TODO Replace this code to use a Student objects instead of a dictionary objects (Done)
            ### student = {"FirstName": student_first_name,
            ###            "LastName": student_last_name,
            ###            "CourseName": course_name}
            student = Student(student_first_name=student_first_name,
                              student_last_name=student_last_name,
                              course_name=course_name)
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            print("Please enter option 3 to save the data!")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was not the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        print("\nThe data was written to the file!")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")
