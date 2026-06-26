'''tuples'''

numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])


'''coding challenge'''

numbers = (100, 200, 300)

print(numbers[0])
print(numbers[-1])

'''sets'''
numbers = {10, 20, 30}

numbers.add(40)
numbers.remove(20)
print(numbers)
print(len(numbers))

'''bonus'''
colors = {"red", "blue", "green", "red"}
print(colors)

'''coding challenge'''
numbers = {100, 200, 300}

numbers.add(400)
numbers.remove(200)
print(numbers)
print(len(numbers))

'''Dictionaries'''
student = {
    "name": "Swathi",
    "age": 22
}
student["city"] = "Bangalore"
student["age"] = 23
student.pop("name")
print(student)

'''Bonus'''
employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 50000
}
print(employee.get("name"))
print(employee.get("salary"))

'''coding challenge'''

student = {
    "name": "Anu",
    "age": 21
}
student["course"] = "Python"
student["age"] = 22
student.pop("name")
print(student)
