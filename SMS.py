print("----WELCOME TO SCHOOL MANAGEMENT SYSTEM----\n")
n=str(input("ENTER YOUR NAME HERE:"))
print(f"HI {n} I HOPE YOUR'E FINE HERE'S THE OPTIONS AVAILAIBLE IN OUR SYSTEM")
students=[]
def newstudent():
    import csv
    print("GIVE YOUR DETAILS MENTIONED BELOW:\n")
    ROLL=int(input("ROLL NO.:"))
    NAME=str(input("NAME:"))
    CLASS=str(input("CLASS:"))
    AGE=int(input("AGE:"))
    ADDRESS=str(input("ADDRESS:"))
    PHONE=str(input("PHONE:"))
    GMAIL=str(input("GMAIL:"))
    print("-----MARKS-----\n")
    ENGLISH=str(input("ENGLISH:"))
    MATHS=str(input("MATHS:"))
    SCIENCE=str(input("SCIENCE:"))
    SOCIAL=str(input("SOCIAL:"))
    COMPUTER=str(input("COMPUTER:"))
    ISLAMIC=str(input("ISLAMIC:"))

    student = {"ROLL": ROLL ,"NAME":NAME ,"CLASS":CLASS ,"AGE":AGE ,"ADDRESS":ADDRESS,"PHONE":PHONE,"GMAIL":GMAIL}
    studentt={"ROLL":ROLL,"ENGLISH":ENGLISH,"MATHS":MATHS,"SCIENCE":SCIENCE,"SOCIAL":SOCIAL,"COMPUTER":COMPUTER,"ISLAMIC":ISLAMIC}
    print(student)
    print(studentt)
#    HERE WE USE LIST TO STORE VALUE BECAUSE LIST STORES MULTIPLE VALUES BUT DICTIONARY DOES'NT
    students.append(student)  
    students.append(studentt)
    try:
            with open("C:/Users/Subhani/Downloads/muslim_students.csv", "a",newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["ROLL","NAME", "CLASS", "AGE","ADDRESS","PHONE","GMAIL"])
                writer.writerow(student)
    except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")  
    try:
            with open("C:/Users/Subhani/Downloads/student_marks.csv", "a",newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["ROLL","ENGLISH","MATHS", "SCIENCE", "SOCIAL","COMPUTER","ISLAMIC"])
                writer.writerow(studentt)

    except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")  

    print("------THANKS FOR USING OUR SERVICE------")
def viewstudent():
    import csv
    print("IF YOU WANT TO VIEW ALL STUDNTS CHOOSE 1. AND IF YOU WANT TO SEARCH STUDENT CHOOSE 2. ")
    print("1.ALL STUDENT LIST")
    print("2.GO TO 3. ON MAIN OPTIONS")
    c=int(input("ENTER YOUR CHOICE :"))
    if c==1:
        #  HERE WER'E MANUALLY ATTACHING FILE USING IMPORT,OPEN.....
         try:
            with open("C:/Users/Subhani/Downloads/muslim_students.csv", "r") as file:
                print("\n----- FULL FILE CONTENT -----\n")
                data = file.read()
                print(data)
                print("\n--------------------------------")
         except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")
    else:
        print("EXIT")
        print("----THANKS FOR USING OUR SERVICE----")
def searchstudent():
    import csv
    print("FOR SEARCHING STUDENT ENTER YOUR ROLL NO. BELOW ")
    r=str (input("ROLL NO:"))
    try:
            with open("C:/Users/Subhani/Downloads/muslim_students.csv", "r") as file:
                print("\n----- FULL FILE CONTENT -----\n")
                reader=csv.reader(file)
                found = False
                for parts in reader:
                 if len(parts)<7:
                  continue
                 ROLL,NAME,CLASS,AGE,ADDRESS,PHONE,GMAIL= parts
                 if str (ROLL)==r:
                     print("STUDENT FOUND WITH THIS ROLL NO",r) 
                     print(f"NAME   : {NAME}")
                     print(f"CLASS  : {CLASS}")
                     print(f"ROLL   : {ROLL}")
                     print(f"AGE    : {AGE}")
                     print(f"PHONE  : {PHONE}")
                     print(f"ADDRESS: {ADDRESS}")
                     print(f"GMAIL  : {GMAIL}")
                     found = True      
            if  not found:
                print("----NO STUDENT FOUND WITH THIS ROLL NO.",r)              
    except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")
    try:
            with open("C:/Users/Subhani/Downloads/student_marks.csv", "r") as file:
                print("\n----- FULL FILE CONTENT -----\n")
                reader=csv.reader(file)
                found = False
                for parts in reader:
                 if len(parts)!=7:
                  continue
                 ROLL,ENGLISH,MATHS,SCIENCE,SOCIAL,COMPUTER,ISLAMIC= parts
                 if str (ROLL)==r:
                     print("STUDENT FOUND WITH THIS ROLL NO",r) 
                     print(f"ENGLISH : {ENGLISH}")
                     print(f"MATHS   : {MATHS}")
                     print(f"SCIENCE : {SCIENCE}")
                     print(f"SOCIAL  : {SOCIAL}")
                     print(f"COMPUTER: {COMPUTER}")
                     print(f"ISLAMIC : {ISLAMIC}")
                     found = True      
            if  not found:
                print("----NO MARKS FOUND WITH THIS ROLL NO.",r)
               
    except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")
   
def delstudent():
     import csv
     print("ENTER YOUR ROLL NO OF STUDENT YOU WANT TO DELETE:")
     d=str(input("ROLL NO:"))
     try:
            with open("C:/Users/Subhani/Downloads/muslim_students.csv", "r") as file:
                lines=file.readlines()
                found=False
            with open("C:/Users/Subhani/Downloads/muslim_students.csv", "w") as file:
             for line in lines:
                 line=line.strip()
                 if line.startswith("ROLL"):  
                    file.write(line + "\n")
                    continue

                
                 parts = line.split(",")
                 student_roll = parts[0]  

            
                 if student_roll == str(d):
                    found = True
                    continue  

                
                 file.write(line + "\n")
            if found:
                  print("----STUDENT IS DELETED SUCESSFULLY----")
            else:
                    print("STUDENT IS NOT DELETED")
     except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")
         
     try:
            with open("C:/Users/Subhani/Downloads/student_marks.csv", "r") as file:
                lines=file.readlines()
                found=False
            with open("C:/Users/Subhani/Downloads/student_marks.csv", "w") as file:
             for line in lines:
                 line=line.strip()
                 if line.startswith("ROLL"):  
                    file.write(line + "\n")
                    continue

                
                 parts = line.split(",")
                 student_roll = parts[0]  

            
                 if student_roll == str(d):
                    found = True
                    continue  

                
                 file.write(line + "\n")
            if found:
                  print("----STUDENT MARKS IS DELETED SUCESSFULLY----")
                  print("----THANKS FOR USING OUR SERVICE----")
            else:
                    print("STUDENT IS NOT DELETED")
     except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")

def marksofstudent():
    print("-----SESSION MARKS OF STUDENT-----")
    import csv
    print("ENTER ROLL OF YOUR STUDENT :")
    r=str (input("ROLL NO:"))
    try:
            with open("C:/Users/Subhani/Downloads/muslim_students.csv", "r") as file:
                print("\n----- FULL FILE CONTENT -----\n")
                reader=csv.reader(file)
                found = False
                for parts in reader:
                 if len(parts)<7:
                  continue
                 ROLL,NAME,CLASS,AGE,ADDRESS,PHONE,GMAIL= parts
                 if str (ROLL)==r:
                      print("---- STUDENT FOUNDED ----")
                      print(f"NAME   : {NAME}")
                      found = True
                if not found:
                    print("----NO STUDENT FOUND WITH THIS ROLL NO.",r)
               
    except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.\n")

    try:
        with open("C:/Users/Subhani/Downloads/student_marks.csv","r") as file:
          reader=csv.reader(file)
          found=False
          for parts in reader :
              if len(parts)!=7:
                  continue
              ROLL,ENGLISH,MATHS,SCIENCE,SOCIAL,COMPUTER,ISLAMIC=parts
              if  (ROLL)==r:
                  print("-----FULL FILE CONTENT-----\n")
                  print(f"ENGLISH : {ENGLISH}")
                  print(f"MATH    : {MATHS}")
                  print(f"SCIENCE : {SCIENCE}")
                  print(f"SOCIAL  : {SOCIAL}")
                  print(f"COMPUTER: {COMPUTER}")
                  print(f"ISLAMIC : {ISLAMIC}\n")
                  TOTAL=int(ENGLISH)+int(MATHS)+int(SCIENCE)+int(SOCIAL)+int(COMPUTER)+int(ISLAMIC)
                  PERCENTAGE=TOTAL/600*100
                  print("-----RESULT-----\n")
                  print(f"TOTAL      : {TOTAL} ")
                  print(f"PERCENTAGE : {PERCENTAGE}")
                  if PERCENTAGE>90:
                       print("GRADE      : A")
                  elif PERCENTAGE>80:
                       print("GRADE      : B")
                  elif PERCENTAGE>70:
                       print("GRADE      : C") 
                  elif PERCENTAGE>60:
                       print("GRADE      : D")
                  else :
                       print("PERCENTAGE IS VERY LOW NEED IMPROVEMENT")                         
                  found = True
        if not found:
                  print("-----MARKS NOT FOUND-----")
    except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.\n")    
def newmarks():
    import csv
    print("-----STUDENT MARKS-----")
    ROLL=int(input("ROLL NO.:")) 
    ENGLISH=str(input("ENGLISH:"))
    MATHS=str(input("MATHS:"))
    SCIENCE=str(input("SCIENCE:"))
    SOCIAL=str(input("SOCIAL:"))
    COMPUTER=str(input("COMPUTER:"))
    ISLAMIC=str(input("ISLAMIC:"))
    studentt={"ROLL":ROLL,"ENGLISH":ENGLISH,"MATHS":MATHS,"SCIENCE":SCIENCE,"SOCIAL":SOCIAL,"COMPUTER":COMPUTER,"ISLAMIC":ISLAMIC}
    students.append(studentt)
    print(studentt)
    try:
            with open("C:/Users/Subhani/Downloads/student_marks.csv", "a",newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["ROLL","ENGLISH","MATHS", "SCIENCE", "SOCIAL","COMPUTER","ISLAMIC"])
                writer.writerow(studentt)

    except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")  
    print("------THANKS FOR USING OUR SERVICE------")
def viewallmarks():
    import csv
    try:
            with open("C:/Users/Subhani/Downloads/student_marks.csv", "r") as file:
                print("\n----- FULL FILE CONTENT -----\n")
                data = file.read()
                print(data)
                print("\n--------------------------------")
    except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")
   
    print("FOR SEARCHING STUDENT ENTER YOUR ROLL NO. BELOW ")
    r=str (input("ROLL NO:"))
    try:
            with open("C:/Users/Subhani/Downloads/student_marks.csv", "r") as file:
                print("\n----- FULL FILE CONTENT -----\n")
                reader=csv.reader(file)
                found = False
                for parts in reader:
                 if len(parts)!=7:
                  continue
                 ROLL,ENGLISH,MATHS,SCIENCE,SOCIAL,COMPUTER,ISLAMIC= parts
                 if str (ROLL)==r:
                     print("STUDENT FOUND WITH THIS ROLL NO",r) 
                     print(f"ENGLISH : {ENGLISH}")
                     print(f"MATHS   : {MATHS}")
                     print(f"SCIENCE : {SCIENCE}")
                     print(f"SOCIAL  : {SOCIAL}")
                     print(f"COMPUTER: {COMPUTER}")
                     print(f"ISLAMIC : {ISLAMIC}")
                     found = True      
            if  not found:
                print("----NO MARKS FOUND WITH THIS ROLL NO.",r)
    except FileNotFoundError:
            print("ERROR: File NOT found. Check the file path again.")
     
while True:
 print("-------------------------------------------------------------------------------------------")
 print("WELCOME IN OUR SERVICE")
 print("WHAT SHOULD I DO FOR YOU:")
 print("1.NEW STUDENT")
 print("2.VIEW STUDENT")
 print("3.SEARCH STUDENT")
 print("4.DELETE STUDENT")
 print("5.RESULT OF STUDENT")
 print("6.NEW MARKS")
 print("7.VIEW ALL MARKS")
 print("8.EXIT")
 print("ENTER YOUR CHOICE:")
 b=str(input("CHOICE:"))
 if b=="1":
     newstudent()
 elif b=="2":
     viewstudent()
 elif b=="3":
     searchstudent()
 elif b=="4":
     delstudent()
 elif b=="5":
     marksofstudent()    
 elif b=="6":
     newmarks()
 elif b=="7":
      viewallmarks()
 elif b=="8":
      print("-----EXIT-----")
      break
 else:
     print("-----INVALID INPUT-----") 



    
     
      





       
      





   


    
