########################################################################
# Allene Cates
#
# M02 Case Study.py
#
# This app determines if a student is on the deans list or honor roll based on GPA
#
########################################################################


last_name = input("Please enter the students last name or ZZZ to quit: ") #Get last name

#quit
if last_name == "ZZZ":
    print("Goodbye!")
    quit()

first_name = input("Please enter the students first name: ") #Get first name
gpa = float(input("Please enter the students GPA: ")) #Get GPA

#Determine what award (if any) the student will be receiving
while True:
    if gpa >= 3.5:
        print("This student is on the Dean's List!")
        break
    elif gpa >= 3.25:
        print("This student is on the Honor Roll!")
        break
    elif gpa < 3.25:
        print("This student did not receive either honorific.")
        break