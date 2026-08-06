'''

Course : MScIT Sem-3
Roll No :250160450347
Name : Shekh Vishal
Practical: Week1 Practical 3
Description:- Student Performance Analytics System Develop a Python program to manage and analyse the academic performance of a class.
                The program should:
                Accept the details of 10 students, including:
                    Roll Number
                    Name
                    Marks in 5 subjects
                Store the student information using appropriate Python data structures (lists, tuples, and dictionaries).
                Calculate for each student:
                    Total Marks
                    Percentage
                    Grade (A, B, C, D, F)
                Display:
                    Class average percentage
                    Highest scorer(s)
                    Lowest scorer(s)
                    Students scoring above the class average
                    Students who failed in one or more subjects
                Create a dictionary where:
                    Key = Grade
                    Value = List of students belonging to that grade
                Display the names of students in alphabetical order without modifying the original records.
                Find the second-highest scorer without sorting the entire dataset.
                Display the subject in which the class has obtained the highest average marks.
                Remove duplicate student names (if any) and report the duplicate entries.


                    
 '''



# dictionary
my_dict = dict()

# lists
std_rollNo_list = list()
std_name_list = list()

c_mark = list()
java_mark = list()
python_mark = list()
dbms_mark = list()
os_mark = list()

mark_of_sum_list = list()
percentage_list = list()
grade_list = list()


# function insert
def insert_data(n_std):

    for i in range(0, n_std):

        print()
        Roll_No = input("Roll no : ")
        

        if Roll_No in my_dict:
            print(Roll_No, "already inserted.")
            continue

        Name = input("Student name : ")

        c = int(input("C mark (0-100) : "))
        java = int(input("Java mark (0-100) : "))
        python = int(input("Python mark (0-100) : "))
        dbms = int(input("DBMS mark (0-100) : "))
        os = int(input("OS mark (0-100) : "))


        if ((c < 0 or c > 100) or (java < 0 or java > 100) or (python < 0 or python > 100) or (dbms < 0 or dbms > 100) or (os < 0 or os > 100)):
            print("Please enter valid marks (0-100).")
            continue


        # store in lists
        std_rollNo_list.append(Roll_No)
        std_name_list.append(Name)

        c_mark.append(c)
        java_mark.append(java)
        python_mark.append(python)
        dbms_mark.append(dbms)
        os_mark.append(os)

        total = c + java + python + dbms + os        
        p = total / 5


        # grade
        if p >= 80 and p <= 100:
            grade = "A"

        elif p >= 70 and p <= 79:
            grade = "B"

        elif p >= 60 and p <= 69:
            grade = "C"

        elif p >= 40 and p <= 59:
            grade = "D"

        else:
            grade = "F"


        mark_of_sum_list.append(total)
        percentage_list.append(p)
        grade_list.append(grade)


    # tuple casting
    RollNo_tuple = tuple(std_rollNo_list)
    Name_tuple = tuple(std_name_list)

    C_tuple = tuple(c_mark)
    Java_tuple = tuple(java_mark)
    Python_tuple = tuple(python_mark)
    DBMS_tuple = tuple(dbms_mark)
    OS_tuple = tuple(os_mark)

    sum_tuple = tuple(mark_of_sum_list)
    percentage_tuple = tuple(percentage_list)
    grade_tuple = tuple(grade_list)


    # store in dictionary
    for j in range(len(RollNo_tuple)):

        student = RollNo_tuple[j]

        my_dict[student] = {

            "Roll_No": RollNo_tuple[j],

            "Name": Name_tuple[j],

            "mark": {
                "C": C_tuple[j],
                "Java": Java_tuple[j],
                "Python": Python_tuple[j],
                "DBMS": DBMS_tuple[j],
                "OS": OS_tuple[j]
            },

            "Total_mark": sum_tuple[j],

            "Percentage": percentage_tuple[j],

            "Grade": grade_tuple[j]
        }


    print()
    print(n_std, "student record successfully inserted.")
    print()


# function show data
def print_data():

    print(my_dict)


# function class 
def class_average():

    if len(percentage_list) == 0:
        print("No student record found...")
        return

    avg = sum(percentage_list) / len(percentage_list)

    print()
    print("___________________________________________________________________")
    print()
    print("===== Class Average Percentage =====")
    print("Class Average :", avg, "%")
    print()
    print("___________________________________________________________________")
    print()


# function highest scorer
def highest_marks():

    if len(mark_of_sum_list) == 0:
        print("No student record found...")
        return

    highest = max(mark_of_sum_list)

    print()
    print()
    print("___________________________________________________________________")
    print()
    print("===== Highest Scorer(s) =====")

    for i in range(len(mark_of_sum_list)):

        if mark_of_sum_list[i] == highest:

            print("Roll No :", std_rollNo_list[i])
            print("Name :", std_name_list[i])
            print("Total Marks :", mark_of_sum_list[i])
            print("Percentage :", percentage_list[i])
            print("Grade :", grade_list[i])
            print()
    print()
    print("___________________________________________________________________")
    print()


# function lowest scorer
def lowest_marks():

    if len(mark_of_sum_list) == 0:
        print("No student record found...")
        return

    lowest = min(mark_of_sum_list)

    print()
    print("___________________________________________________________________")
    print()
    print("===== Lowest Scorer =========")

    for i in range(len(mark_of_sum_list)):

        if mark_of_sum_list[i] == lowest:

            print("Roll No :", std_rollNo_list[i])
            print("Name :", std_name_list[i])
            print("Total Marks :", mark_of_sum_list[i])
            print("Percentage :", percentage_list[i])
            print("Grade :", grade_list[i])
            print()
    print()
    print("___________________________________________________________________")
    print()


# function students above class average
def above_average():

    if len(percentage_list) == 0:
        print("No student record found...")
        return

    avg = sum(percentage_list) / len(percentage_list)
    print()
    print("___________________________________________________________________")
    print()
    print()
    print("===== Students Above Class Average =====")

    for i in range(len(percentage_list)):

        if percentage_list[i] > avg:

            print(std_rollNo_list[i], std_name_list[i], percentage_list[i] )
            
    print()
    print("___________________________________________________________________")
    print()


# function failed students
def failed_students():

    print()
    print("___________________________________________________________________")
    print()
    print("========= Failed Students =========")

    for i in range(len(std_rollNo_list)):

        if (c_mark[i] < 40 or  java_mark[i] < 40 or  python_mark[i] < 40 or dbms_mark[i] < 40 or  os_mark[i] < 40):

            print(std_rollNo_list[i], std_name_list[i] )
    print()
    print("___________________________________________________________________")
    print()


# function grade dictionary
def grade_dictionary():

    grade_dict = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "F": []
    }

    for i in range(len(std_name_list)):

        grade_dict[grade_list[i]].append(std_name_list[i])

    
    print()
    print("___________________________________________________________________")
    print()
    print("===== Grade Dictionary ===========")
    print(grade_dict)
    
    print()
    print("___________________________________________________________________")
    print()


# function alphabetical names
def alphabetical_names():

    names = sorted(std_name_list)

    print()
    print("___________________________________________________________________")
    print()
    print("===== Alphabetical Student Names ===============")

    for name in names:
        print(name)
    
    print()
    print("___________________________________________________________________")
    print()


# function second highest scorer

def second_highest():

    if len(mark_of_sum_list) < 2:
        print("Not enough student records...")
        return

    highest = -1
    second = -1

    for mark in mark_of_sum_list:

        if mark > highest:

            second = highest
            highest = mark

        elif mark > second and mark != highest:

            second = mark


    print()
    print("___________________________________________________________________")
    print()
    print("===== Second Highest Scorer =====")

    for i in range(len(mark_of_sum_list)):

        if mark_of_sum_list[i] == second:

            print("Roll No :", std_rollNo_list[i])
            print("Name :", std_name_list[i])
            print("Total Marks :", mark_of_sum_list[i])
            
    print()
    print("___________________________________________________________________")
    print()


# function highest average subject
def highest_subject_average():

    if len(std_rollNo_list) == 0:
        print("No student record found...")
        return

    c_avg = sum(c_mark) / len(c_mark)
    java_avg = sum(java_mark) / len(java_mark)
    python_avg = sum(python_mark) / len(python_mark)
    dbms_avg = sum(dbms_mark) / len(dbms_mark)
    os_avg = sum(os_mark) / len(os_mark)


    subject_avg = {
        "C": c_avg,
        "Java": java_avg,
        "Python": python_avg,
        "DBMS": dbms_avg,
        "OS": os_avg
    }


    highest = max(subject_avg.values())


    print()
    print("___________________________________________________________________")
    print()
    print("===== Highest Average Subject ============")

    for subject in subject_avg:

        if subject_avg[subject] == highest:

            print("Subject :", subject)
            print("Average :", highest)
            
    print()
    print("___________________________________________________________________")
    print()


# function duplicate names
def duplicate_names():

    s = set()
    duplicate = set()


    for name in std_name_list:

        if name in s:

            duplicate.add(name)

        else:

            s.add(name)


    print()
    print("===== Duplicate Student Names =====")


    if len(duplicate) == 0:

        print("No duplicate names found.")

    else:

        print("Duplicate Names :", duplicate)


   
    unique_names = list(set(std_name_list))

    print("Names After Removing Duplicate :", unique_names)


# menu base code

while 1:

    print()
    print("1. Insert")
    print("2. Show Data")
    print("3. Class Average Percentage")
    print("4. Highest Scorer")
    print("5. Lowest Scorer")
    print("6. Above Class Average Students")
    print("7. Failed Students")
    print("8. Grade Dictionary")
    print("9. Alphabetical Student Names")
    print("10. Second Highest Scorer")
    print("11. Highest Average Subject")
    print("12. Duplicate Student Names")
    print("13. Exit")


    choice = int(input("Enter choice (1-13) : "))

    print()


    match(choice):

        case 1:

            n_std = int(input("Enter the Number of Student : "))

            if n_std > 10:
                print("Only 10 students allowed.")

            else:
                insert_data(n_std)

        case 2:

            print_data()

        case 3:

            class_average()

        case 4:

            highest_marks()

        case 5:
            lowest_marks()

        case 6:
            above_average()

        case 7:
            failed_students()


        case 8:

            grade_dictionary()

        case 9:
            alphabetical_names()


        case 10:
            second_highest()

        case 11:
            highest_subject_average()

        case 12:
            duplicate_names()

        case 13:
            break

        case _:

            print("Invalid Choice.........")

