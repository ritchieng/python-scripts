# Find the smallest and largest numbers
# This allows the user to enter a list of numbers until the user types done or press enter then the prompt would stop
# Author: Ritchie Ng

largest = None
smallest = None

while True:
    num = raw_input('Enter a number: ')

    # Handle edge cases
    if num == 'done':
        break
    # Allows user to press enter to complete
    if len(num) < 1:
        break

    # Try and Except to catch input errors
    try:
        num = float(num)
    except:
        print 'Invalid Input'
        # Jumps to the start of the loop without running the code below
        continue

    # This will be permanently false after the first iteration
    if smallest is None:
        smallest = num
    # Replaces the iteration variable with smaller input num
    if num < smallest:
        smallest = num

    # This will be permanently false after the first iteration
    if largest is None:
        largest = num
    # Replaces the iteration variable with larger input num
    elif num > largest:
        largest = num

print "Maximum number:", largest
print "Smallest number:", smallest


