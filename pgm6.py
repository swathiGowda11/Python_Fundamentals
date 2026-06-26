'''Write the voter eligibility program with:

age
voter ID (yes/no)
nested if'''
age = int(input("Enter your age:"))
voter_ID = input("Do you have voter_id?(yes/no):")

if age>=18:
    if voter_ID.lower() == "yes":
        print("Eligible for voting")
    else:
        print("Not eligible for voting as you dont have voter_id")
else:
    print("Not eligible for voting as you are not 18 years old")
