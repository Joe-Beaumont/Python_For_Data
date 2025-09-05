from collections import namedtuple
from functools import reduce


def my_first_function(string):
    print(f"I love {string}")

my_first_function("Dawn")

def tripler(number):
    return number*3

print(tripler(3))
print(tripler(4))
print(tripler(5))

def greet(name):
    return f"Hello, {name}"

print(greet("Joe"))

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(5))
print(is_even(6))

def repeat_word(word, times):
        print(word)


print(repeat_word("hello", 5))


import math
def circle_perimeter(radius):
    return 2 * math.pi * radius

def circle_area(radius):
    return math.pi * radius ** 2

circle_perimeter_lambda = lambda r: 2 * math.pi * r
circle_area_lambda = lambda r: math.pi * r**2

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

triangle_area_lambda = lambda a, b, c: math.sqrt((a + b + c)/2 * ((a + b + c)/2 - a) * ((a + b + c)/2 - b) * ((a + b + c)/2 - c))

# lambda functions
numbers = [2, 5, 7, 32, 100, 9, 56, 74, 97, 22, 13, 80]

numbers = list(filter(lambda x: x % 2 ==0, numbers))
numbers = list(map(lambda x: x * 3, numbers))
numbers = reduce(lambda a, b: a + b, numbers)
print(numbers)

# reading csv

import csv
rows = []

with open('../Day 3/employers.csv', newline="")as csvfile: #reading files
    csvreader = csv.reader(csvfile) #establishing headers
    header = next(csvreader)
    for row in csvreader: #normal loop
        rows.append(row)

print(f"Headers are: {header}")

# write to csv

header = ['Name', 'age']
data = [['Alex', 25], ['Brad', 30], ['Joey', 18]]
with open('../Day 4/student_info.csv', 'w') as csvfile: #creates csv file - w means write mode (otherwise it would try read a non-existant file
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(data)

students = []

with open('../Day 4/student_info.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for student in csvreader:
        students.append(student)

print(students)

# reading as a dictionary (object in js) using DictReader
with open('../Day 3/employers.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row["Name"], row["email"])
        print(row)

#write to csv file using DictWriter

headers = ['Name', 'age']
data = [['Alex', 25], ['Brad', 30], ['Joey', 18]]

with open('../Day 4/student_info.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = headers)

    writer.writeheader()
    for student in data:
        writer.writerow({'Name' : student[0], 'age' : student[1]})

# namedtuple() - when importing a file, we can cast the incoming data to the namedtuple() for easier reading

with open('../Day 3/employers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    Employee = namedtuple("Employee", next(reader), rename=True)
    for row in reader:
        employee = Employee(*row)
        print(employee.Name, employee.Position, employee.email)


# challenge


state_info = []
capitals = {'VIC' : 'Victoria',
            'NSW' : 'New South Wales',
            'SA' : 'Sydney',
            'WA' : 'Philadelphia',
            'Tasmania' : 'Taz',
            'Queensland' : 'Queenie',
            'ACT' : 'Java',
            'NT' : 'Wellington'
            }

with open('../Day 3/australia.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        state = row["State"]
        population = int(row["Population"])
        if state in capitals:
            capital = capitals[state]
        else:
            capital = "Unknown"
        row["Capital"] = capital
        state_info.append(row)

print(state_info)

# further challenge

grades = []

with open('../Day 4/studentgrades.csv', 'r', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        grades.append(row)

print(grades)

marks = [int(x["Grade"]) for x in grades]
print(marks)
avg_mark = sum(marks)/len(marks)
max_mark = max(marks)
min_mark = min(marks)
