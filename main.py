# Assignment:
# Write a program to prompt the user to provide an integer which returns the corresponding day of the week.
# If the user enters 1, print "Sunday". If the user enters 2, print "Monday". If the user enters 3, print "Tuesday". If the user enters 4, 
# print "Wednesday". If the user enters 5, print "Thursday". If the user enters 6, print "Friday". If the user enters 7, print "Saturday".
# If the user inputs a number less than 1 or greater than 7, direct the user to input an integer within the proper range of 1 - 7.
# IMPORTANT: Your program must make use of a list to contain the days of the week, not a series of 'if statements'.

# Get user input
number = input('Please enter an integer between 1 and 7: ')

# Make sure input is an integer
try:
    number_int = int(number)
except ValueError:
    print("Please enter an integer.")

# Make sure integer is between 1 and 7
if 1 <= number_int <= 7:
    pass
else:
    print("Make sure the integer is between 1 and 7!")
    print(f'{number_int} is not between 1 and 7!')
    raise SystemExit()

# Make list of days
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Print specified day
print(f'{days[number_int-1]}')

# Comment with name, date, and assignment name redacted
