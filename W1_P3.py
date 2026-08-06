'''

Course : MScIT Sem-3
Roll No :250160450347
Name : Shekh Vishal
Practical: Week1 Practical 1
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


#dict
my_dict=dict();

student=0
my_dict[student] = {}
my_dict[student]['mark'] = {}

#list
std_rollNo_list=list();
std_name_list=list();
std_age_list=list();
c_mark=list()
java_mark=list()
python_mark=list()
mark_of_sum_list=list()
percentage_list=list()
result_list=list()


#function insert
def insert_data(n_std):
    result=""
    
    for i in range(0,n_std):
        print()
        Roll_No=input(" Roll no:")
        
    
        if Roll_No in my_dict:
            print(Roll_No, "already inserted.")
            continue
        Name=input("sudent name ...:")
        Age=int(input("student age...:"))
        c=eval(input("C mark:(1-100) :"))
        java=eval(input("java mark:(1-100) :"))
        python=eval(input("pyton mark:(1-100) :"))
        
        
        if ((c < 0 or c > 100) or (java < 0 or java > 100) or (python < 0 or python > 100)):
            print("Please enter valid marks.. (0-100).")
            break
           
        std_rollNo_list.append(Roll_No)
        std_name_list.append(Name)
        std_age_list.append(Age)
        c_mark.append(c)
        java_mark.append(java)
        python_mark.append(python)
        
        t_sum=c+java+python;
        
        
              
        if(c<40 or java<40 or python<40):
            p = 0
            result = "Fail"
        else:
            p = t_sum / 3
            result = "Pass"   
            
        mark_of_sum_list.append(t_sum)
        percentage_list.append(p)
        result_list.append(result) 
            
        
        
    #tuple castting
    RollNo_tuple = tuple(std_rollNo_list)
    Name_tuple = tuple(std_name_list)
    Age_tuple = tuple(std_age_list)
    C_tuple = tuple(c_mark)
    Java_tuple = tuple(java_mark)
    python_tuple = tuple(python_mark)
    sum_tuple = tuple(mark_of_sum_list)
    p_tuple = tuple(percentage_list)
    result_tuple = tuple(result_list)
    
  
              
    for j in range(len(RollNo_tuple)):

        student = RollNo_tuple[j]

        my_dict[student] = {
            "Roll_No": RollNo_tuple[j],
            "Name": Name_tuple[j],
            "Age": Age_tuple[j],
            "mark": {
                "C": C_tuple[j],
                "Java": Java_tuple[j],
                "Python": python_tuple[j]
            },
            "Total_mark": sum_tuple[j],
            "Percentage": p_tuple[j],
            "Result": result_tuple[j]
        }

                 
        
    print()            
    print(n_std,"student record succefully inserted........")
    print()
    


# function update
def update_data(Roll_No):

   
    if Roll_No not in my_dict:
        print("Student Record Not Found...")
        return

    index = std_rollNo_list.index(Roll_No)
    

    Name = input("Enter New Name : ")
    Age = int(input("Enter New Age : "))
    c = int(input("Enter New C Marks : "))
    java = int(input("Enter New Java Marks : "))
    python = int(input("Enter New Python Marks : "))

    if (c < 0 or c > 100) or (java < 0 or java > 100) or (python < 0 or python > 100):
        print("Please Enter Valid Marks (0-100)")
        return

    # Update Lists
    std_name_list[index] = Name
    std_age_list[index] = Age
    c_mark[index] = c
    java_mark[index] = java
    python_mark[index] = python

    total = c + java + python
    mark_of_sum_list[index] = total

    if c < 40 or java < 40 or python < 40:
        percentage_list[index] = 0
        result_list[index] = "Fail"
    else:
        percentage_list[index] = total / 3
        result_list[index] = "Pass"


    # Update 
    my_dict[Roll_No]["Name"] = Name
    my_dict[Roll_No]["Age"] = Age
    my_dict[Roll_No]["mark"]["C"] = c
    my_dict[Roll_No]["mark"]["Java"] = java
    my_dict[Roll_No]["mark"]["Python"] = python
    my_dict[Roll_No]["Total mark"] = total
    my_dict[Roll_No]["Percentage"] = percentage_list[index]
    my_dict[Roll_No]["Result"] = result_list[index]

    print("\nStudent Record Updated Successfully...\n")


#print dict
def print_data():
    print(my_dict)
        

#function mark_sheet
def mark_sheet(Roll_No):
    if Roll_No in my_dict:
        student=Roll_No;
        print(" " )
        print(" " )
        print(" " )
        print("========== MARK SHEET ==========" )
        print("--------------------------------------------------------------------------------------------------")
        print("Roll Number :",Roll_No)
        print("Student Name :",my_dict[student]['Name'])
        print("Student Age :", my_dict[student]['Age'])
        print("_________________________________________________________________________________")

        print("_____________________ SUBJECT  ___________________________________")
        print("C :     ", my_dict[student]['mark'] ['C'])
        print("JAVA :  ",  my_dict[student]['mark'] ['Java'])
        print("PYTHON :", my_dict[student]['mark'] ['Python'] )

        print("_____________________________________________________")

        print("Total mark :",my_dict[student]['Total_mark'])
        print("percentage :",my_dict[student]['Percentage'])
        print("Retult :", my_dict[student]['Result'])
        print("--------------------------------------------------------------------------------------------------")
        print(" " )
        print(" " )
        print(" " )
        
    else:
        print("not found recorde......................");


#function highest_marks
def highest_marks():

    if len(mark_of_sum_list) == 0:
        print("No student record found...")
        return

    highest = max(mark_of_sum_list)
    index = mark_of_sum_list.index(highest)
    print("___________________________________________________________________")
    print()
    print("\n===== Highest Marks =====")
    print()
    print("Roll No :", std_rollNo_list[index])
    print("Name :", std_name_list[index])
    print("Age :", std_age_list[index])
    print("C Marks :", c_mark[index])
    print("Java Marks :", java_mark[index])
    print("Python Marks :", python_mark[index])
    print("Total Marks :", mark_of_sum_list[index])
    print("Percentage :", percentage_list[index])
    print("Result :", result_list[index])
    print()
    print("___________________________________________________________________")

   
        
    

# function lowest_marks
def lowest_marks():

    if len(mark_of_sum_list) == 0:
        print("No student record found...")
        return

    lowest = min(mark_of_sum_list)
    index = mark_of_sum_list.index(lowest)
    print()
    print("___________________________________________________________________")
    print()
    print("===== Lowest Marks =====")
    print("Roll No :", std_rollNo_list[index])
    print("Name :", std_name_list[index])
    print("Age :", std_age_list[index])
    print("C Marks :", c_mark[index])
    print("Java Marks :", java_mark[index])
    print("Python Marks :", python_mark[index])
    print("Total Marks :", mark_of_sum_list[index])
    print("Percentage :", percentage_list[index])
    print("Result :", result_list[index])
    print()
    print("___________________________________________________________________")
    
    
# function AVG
def average_marks():

    if len(mark_of_sum_list) == 0:
        print("No student record found...")
        return

    avg = sum(mark_of_sum_list) / len(mark_of_sum_list)

    print("===== Average Marks =====")
    print("Average Marks :", avg)
    
    
    
    
#manu base code

while 1:
    print("1. insert");
    print("2. update");
    print("3. Highest marks");
    print("4. Lowest marks ");
    print("5. Average marks ");
    print("6. show data");
    print("7. Mark sheet print")
    print("8. exit");
    choice=int(input("enter choice(1-8):"))
    print()
    match(choice):
        case 1 :
            
            n_std=int(input("Enter the Number of Student :"))
            insert_data(n_std);
            
        case 2:
            
            Roll_No=input("enter the update student Roll no:")
           
            update_data(Roll_No)
            
            
        case 3:
           
            highest_marks();
        case 4:
           
            lowest_marks();
            
        case 5:
           
            average_marks();
           
        case 6 :
            print_data()

        case 7:
            Roll_No=input("enter the student Roll no for search mark sheet :")
            mark_sheet(Roll_No);
                
        case 8:
             break;
        case _:
            print("Invalid Choice...")