########################################################################
# Allene Cates
#
# M02 Case Study.py
#
# This app determines if a student is on the deans list or honor roll based on GPA
#
########################################################################

last_name = input("Please enter the students last name or ZZZ to quit: ")
score = float(input("Please enter the students GPA: "))

if score >= 3.5:
    print("This student is on the Dean's List!")
elif score >= 3.25:
    print("This student is on the Honor Roll!")
