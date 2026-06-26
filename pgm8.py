'''A student passes if:

Marks are 40 or above OR
They have a sports quota (yes/no).'''
marks = int(input("Enter your marks:"))
sports_quota = input("Do you have sports_quota?(yes/no:")

if marks >= 40 or sports_quota.lower() == "yes":
    print("The student has passed")
else:
    print("The student has failed")