# Practice Generators
# Write a Python program to implement a sequence of even numbers less than 20 using python generators.
# Do not create function with additional parameter.
# The tests are designed in a way that they will internally call the even_numbers() function.
def even_numbers():
    # generate  the even_numbers < 20
    num = 0
    while num < 20:
        if num%2 == 0:
            yield num
        num += 1

print(list(even_numbers())) #output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]