'''Takes the user's age.
Takes whether they have a driving license (yes/no).
A person can drive only if:
Age is 18 or above and
They have a driving license.
Otherwise print that they cannot drive.'''
age = int(input("Enter your age:"))
driving_license =input("Whether you have driving_license?(yes/no):")

if age>=18 and driving_license.lower() == "yes":
    print("you can drive")
else:
    print("you cannot drive")