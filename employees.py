employees = ['Bob', 'Sally', 'Barb', 'Kevin']
for employee in employees:
    if employee == 'Bob':
        print(employee.upper())
    else:
        print(employee.title())

# Checking for Eqaulity
employee = 'bob'
# set value of employee to bob
employee.lower() == 'bob'
# Check whether or not is true or false
# Set to lowercase to make sure case senstitive

employee_available = 'bob'
employee_available = 'sally'

if employee_available != 'bob':
    print("Employee not availabile!")

employee_count = 10
employee_count == 10

print(employee_count)
print("----------------------------")

# if statements
(employee_count >= 25) and (employee_count >= 50)

# using or to check multiple conditions
employee_0 = 22
employee_1 = 18
employee_0 >= 21 or employee_1 >= 21

# checking whether a list contains a value
helanas_employees = ['Blaise Roberts', 'Taylor Perkins', 'Brenden Nosrat',
                     'Jeremy Bakker', 'Miriam Rosenbaum']
is_current_employee = 'Blaise Roberts' in helanas_employees
print(is_current_employee)
print("----------------------------")

# checkint whether a value is not in a list
current_employees = ['Brenden Nosrat', 'Blaise Roberts', 'Miriam Rosenbaum']
employee = 'Joe Shmoe'

if employee not in current_employees:
    print(employee.title() + ", you do not have access to the account.")

past_employees = 'Steve Brownlee'
print("Is past_employees == 'Steve Brownlee'?")
print(past_employees == 'Steve Brownlee')

print("\nIs past_employees == 'Joe Shmoe'?")
print(past_employees == 'Joe Shmoe')
print("----------------------------")

# if statements
employee_size = 20
if employee_size >= 19:
    print("You have too many employees")
    print("Can you fire an employee? Employee count too large")
    print("----------------------------")

# if-else
employee_benefit_age = 28
if employee_benefit_age >= 27:
    print("You qualify for benefits!")
    print("Have you signed up for our benefits yet?")
else:
    print("Sorry, you are not old enough for benefits")
    print("Please look elsewhere for coverage")
    print("----------------------------")

# if-elif-else chains
# tax deductions for anyone under age 22 is 0%
# tax deductions for anyone between the age of 23 and 35 is 5%
# tax deductions for anyone age 36 or older is 10%
employee_tax_age = 25
if employee_tax_age < 22:
    print("Your tax deduction is 0%")
elif employee_tax_age < 35:
    print("Your tax deduction is 5%")
else:
    print("Your tax deduction is 10%")

# refactored with deduction in if-elif-else chain
employee_tax_age = 25
if employee_tax_age < 22:
    tax_deduction = 0
elif employee_tax_age < 35:
    tax_deduction = 5
else:
    tax_deduction = 10
print("Your tax deduction amount is " + str(tax_deduction) + "%.")
print("----------------------------")

# multiple elif blocks
employee_tax_age = 77
if employee_tax_age < 22:
    tax_deduction = 0
elif employee_tax_age < 35:
    tax_deduction = 5
elif employee_tax_age > 65:
    tax_deduction = 30
else:
    tax_deduction = 10
print("Your tax deduction amount is " + str(tax_deduction) + "%.")
print("----------------------------")

# omitting the else block
employee_tax_age = 24
if employee_tax_age < 22:
    tax_deduction = 0
elif employee_tax_age < 35:
    tax_deduction = 5
elif employee_tax_age < 36:
    tax_deduction = 20
elif employee_tax_age >= 65:
    tax_deduction = 30
print("Your tax deduction amount is " + str(tax_deduction) + "%.")
print("----------------------------")

# testing multiple conditions, useful for when more then one condition is true
# does not skip any code blocks
requested_employees = ['Ryan Belcher', 'Blaise Roberts', 'Steve Brown Lee',
                       'Justin Short', 'Zach Spence']
company_name_one = 'Tootsies'
company_name_two = 'Roberts'
company_name_three = 'Honky Tonk Central'

if 'Ryan Belcher' in requested_employees:
    print("is an employee at " + str(company_name_one))
if 'Blaise Roberts' in requested_employees:
    print("is an employee at " + str(company_name_two))
if 'Steve Brown Lee' in requested_employees:
    print("is an employee at " + str(company_name_three))

print("\nFinished Assigning Employees!")
print("----------------------------")

# if statements with lists
# checking for special items
for requested_employees in requested_employees:
    if requested_employees == 'Blaise Roberts':
        print("Sorry " + requested_employees + " is not availabile!")
    else:
        print("Adding " + requested_employees + ".")
print("\nFinished adding employees!")
print("----------------------------")

# checking that a list is not empty
requested_employees = []

if requested_employees:
    for requested_employees in requested_employees:
        print("Adding " + requested_employees + ".")
    print("\nFinished adding employees!")
else:
    print("Please add employees to list")
print("----------------------------")

# Using Multiple Lists
available_employees = ['Blaise Roberts', 'Taylor Perkins', 'Steven BrownLee',
                       'Miriam Rosenbaum', 'Joe Shmoe', 'Justin Bieber']

requested_employees = ['Blaise Roberts', 'Taylor Perkins', 'Steven BrownLee']
# requested employees could be tuple if not changing set of data

for requested_employees in requested_employees:
    if requested_employees in available_employees:
        print("Adding" + requested_employees + ".")
    else:
        print("Sorry, " + requested_employees + "not availabile right now.")
print("\nFinished adding employees!")
print("----------------------------")
print("----------------------------")
print("----------------------------")

# Dictionaries
employee_0 = {'title': 'Executive Assistant', 'department': 'Human Resources',
              'salary': '30000'}

print(employee_0['title'])
print(employee_0['department'])
print(employee_0['salary'])
print("----------------------------")

# Accessing Values in a Dictionary
employee_0 = {'name': 'Bob Jones', 'title': 'Vice President of Sales'}
print(employee_0['name'])
new_title = employee_0['title']
print("You were promoted to " + str(new_title) + "!")
print("----------------------------")

# Adding New Key-Value Pairs
employee_0['x_position'] = 0
employee_0['y_position'] = 25
print(employee_0)
print("----------------------------")

# Starting with an Empty Dictionary
# Generally used to store user input or when you write code that generates
# a large number of key value pairs automatically
employee_0 = {}
employee_0['title'] = 'President of Sales'
employee_0['salary'] = 30000

print(employee_0)
print("----------------------------")

# Modifying Values in a Dictionary
employee_0 = {'title': 'President of Sales'}
print("The employee is " + employee_0['title'] + ".")

employee_0['title'] = 'CEO'
print("The employee is now " + employee_0['title'] + ".")
print("----------------------------")

employee_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(employee_1['x_position']))

# Move the employee to the right
# Determine how far to move the employee based on its current speed.
if employee_1['speed'] == 'slow':
    x_increment = 1
elif employee_1['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast employee
    x_increment = 3
# the new position is the old position plus the increment
employee_1['x_position'] = employee_1['x_position'] + x_increment
employee_1['speed'] = 'fast'

print("New x-position: " +
      str(employee_1['x_position']) +
      " " + "speed type:" +
      str(employee_1['speed']))
print("----------------------------")

print("------------REMOVING KEY-VALUE PAIRS----------------")
# Removing Key-Value Pairs
employee_3 = {'title': 'Janitor', 'birthday_month': 3}
print(employee_3)

del employee_3['birthday_month']
print(employee_3)
print("----------------------------")

print("---------A DICTIONARY OF SIMILAR OBJECTS-------------------")
favorite_employee_job = {
    'bob': 'ceo',
    'sarah': 'executive assistant',
    'edward': 'janitor',
    'brenden': 'biologist',
}

for name, job in favorite_employee_job.items():
    print(name.title() + "'s favorite job is " + job.title() + ".")
# print("Bob's favorite job is " +
#       favorite_employee_job['bob'].title() +
#       ".")
print("----------------------------")

print("-------------LOOPING THROUGH A DICTIONARY---------------")
# looping through all key-value pairs
employee_4 = {
    'username': 'bobo',
    'first': 'Bob',
    'last': 'Jones',
}

for k, v in employee_4.items():
    print("\nKey: " + k)
    print("Value: " + v)

print("------------LOOPING THROUGH ALL THE KEYS IN A DICT---------------")
my_employees = ['bob', 'sarah']
for name in favorite_employee_job:
    print(name.title())

    if name in my_employees:
        print("  Hi " + name.title() +
              ", I see your favorite job is " +
              favorite_employee_job[name].title() + "!")
    if 'erin' not in favorite_employee_job.keys():
        print("please sign in!")

print("------------LOOPING THROUGH A DICTIONARY'S KEYS IN ORDER-------------")
favorite_teammate = {
    'jen': 'bob',
    'sarah': 'jen',
    'edward': 'jen',
    'phils': 'Molly',
}

for name in sorted(favorite_teammate.keys()):
    print(name.title() + ", thank you for taking the employee poll")

print("------------LOOPING THROUGH ALL VALUES IN DICTIONARY-------------")
print("The following employees have been mentioned as favorites:")
for name in favorite_teammate.values():
    print(name.title())

print("------------LOOPING THROUGH AND TAKING OUT DUPES-------------")
# taking out duplicates
for name in set(favorite_teammate.values()):
    print(name.title())

print("------------NESTING-------------")
employee_11 = {'title': 'ceo', 'salary': 100000}
employee_12 = {'title': 'marketing manager', 'salary': 50000}
employee_13 = {'title': 'intern', 'salary': 0}

employees = [employee_11, employee_12, employee_13]

for employee in employees:
    print(employee)
print("-------------------------")
# Empty list for storing employees
employees = []

# make 30 CEO employees
for employee_number in range(30):
    new_employee = {'title': 'CEO', 'salary': 30000}
    employees.append(new_employee)

for employee in employees[0:3]:
    if employee['title'] == 'CEO':
        employee['title'] = 'President'
        employee['salary'] = '100000'

# show the first 5 employees:
for employee in employees[:5]:
    print(employee)
print("...")

# Show how many employees have been created
print("Total number of employees: " + str(len(employees)))

print("------------A LIST IN A DICTIONARY-------------")
# store information about employee
employee_profile = {
    'title': 'CEO',
    'responsibilities': ['payroll', 'team management', 'time-off approvals']
}

# Summarize the employee
print("This employee is a " + employee_profile['title'] +
      "with the following responsibilities:")

for responsibility in employee_profile['responsibilities']:
    print("\t" + responsibility)
print("-------------------------")

favorite_employee_activities = {
    'jen': ['lunch', 'team outings'],
    'sarah': ['meetings'],
    'edward': ['hackathons', 'group-coding'],
    'phil': ['one-on-ones', 'cold-calling']
}

# allows every employee to have multiple activities they love because their
# thier activities are now in a list

for name, activities in favorite_employee_activities.items():
    print("\n" + name.title() + "'s favorite employee activities are:")
    for activity in activities:
        print("\t" + activity.title())

print("----------DICTIONARY WITHIN A DICTIONARY---------------")
# the users variable shows how to set a dict within a dict in order to display
# user names for each employee along with first name, last name and location.
# This allows us to change the values within the nested dictionary so we can
# edit and update account information through the key value pairs.

employee_users = {
    'hnosrat': {
        'first': 'helana',
        'last': 'nosrat',
        'location': 'nashville',
    },
    'rbelcher': {
        'first': 'ryan',
        'last': 'belcher',
        'location': 'atlanta',
    },
}

for username, user_info in employee_users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())
print("----------DICTIONARY WITHIN A DICTIONARY---------------")
