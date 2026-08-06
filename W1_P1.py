'''

Course : MScIT Sem-3
Roll No :250160450347
Name : Shekh Vishal
Practical: Week1 Practical 1
Description:-   Student Information System  
                Write a Python program to: 
                ● Create variables to store student information (Roll No., Name, Age, Marks). 
                ● Perform arithmetic operations to calculate total and percentage. 
                ● Use logical operators to determine whether the student has passed (minimum 40 marks in each subject). 
                ● Display the result using formatted output. 
                ● Comment different sections of the program appropriately. 
                
 '''
 
 
while True:
 
 
    c=input("Exit for Enter 0 and Contine For 1 (0-1):")
    
    if(c=='1'):
    
        # Student Info. input
        print()
        print("=======Student Info.=========")
        print()
        Roll_No=input("Student Roll no:")
        Name=input("Sudent name ...:")
        Age=int(input("Student age...:"))

        print()
        print("=======Subject Wise Mark========")
        print()
        c=eval(input("C mark:(1-100) :"))
        java=eval(input("java mark:(1-100) :"))
        python=eval(input("pyton mark:(1-100) :"))



        #condition of valid mark
        if((c>=0 and c<=100) or (java>=0 and java<=100) or (python>=0 and python<=100)):
        
            #conditon for minimum 40 marks in each subject
            if(c<40 or java<40 or python<40): 
            
                print("-----------------------------------------------------------------------------")
                print()
                print("============Student Information=======")
                print()
                
                print("Name    :",Name)
                print("Roll No :",Roll_No)
                print("Age      :",Age)
                print()
               
                print("============Subject Wise Marks=========")
                print()
                print("C      :",c)
                print("JAVA   :",java)
                print("PYTHON :",python)
                print("________________________________________")
                print()
                
                print("Result :Fail")
                print()
                print("-----------------------------------------------------------------------------")
                print()
                
                
            else:
                sum_mark=c+java+python
                p=sum_mark/3;

               
                #result formate
                print("-----------------------------------------------------------------------------")
                print()
                print("============Student Information=======")
                print()
                
                print("Name    :",Name)
                print("Roll No :",Roll_No)
                print("Age      :",Age)
                print()
               
                print("============Subject Wise Marks=========")
                print()
                print("C      :",c)
                print("JAVA   :",java)
                print("PYTHON :",python)
                print("________________________________________")
                print()
                print("Total Mark :",sum_mark)
                print("Total Tercentage :",p)
                print()
                
                print("Result :PASS")
                print()
                print("-----------------------------------------------------------------------------")
                print()
           
        else:
             print("-----------------------------------------------------------------------------")
             print()
             print("please Enter valide mark")
             print()
             print("-----------------------------------------------------------------------------")
    elif(c=='0'):
        break;
    else:
    
        print("Invalid Input Please Enter (0 or 1 )")
        
        
        
    

