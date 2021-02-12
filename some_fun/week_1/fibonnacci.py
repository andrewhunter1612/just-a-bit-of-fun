
starting_number = 1
second_number = 1
output_number = 1
number_of_iterations = int(input("Enter number of iterations: "))

"""
    while the number of iterations is greater than 2
        the output nember will equal the starting number plus a new number
        then to reset the 
        the starting number will become the second number
        the second number will then become the number that i
"""

while number_of_iterations>2:
    output_number = starting_number + second_number
    starting_number = second_number
    second_number = output_number
    number_of_iterations = number_of_iterations -1

print(output_number)