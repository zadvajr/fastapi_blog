#type hinting
#python is a dynamically typed language
#the interpreter does not check the type at compile time but at runtime
#type hinting is a way to tell the interpreter what type the variable should be
#this is not enforced but it is a good practice to use it

#Let's see an example without type hinting
# count = 5
# print(type(count)) #output: <class 'int'>

# count = '5'
# print(type(count)) #output: <class 'str'>

#The basic idea is to annotate the variables, functions to give indications of what they are expecting.
#This is not enforced but it is a good practice to use it.
#You can use static type checkers like mypy to enforce the type hinting
#Type hint aims at improving the developer's productivity and code readability

#Let's see another example
# def total_price(price1, price2):
#     return f"Your total bill is USD {price1 + price2}"

# print(total_price(30,40)) #output: Your total bill is USD 70

#What will happen if we pass a string instead of an integer?
# print(total_price('30','40')) #output: Your total bill is USD 3040

#We can use static type checkers like mypy, pyright, pyre, pylint to enforce the type hinting
#mypy is the most popular static type checker for python
#pip install mypy
#mypy 01_type_hinting.py
#But before we run mypy, we need to add type hinting to the code
#Let's add type hinting to the above code
def total_price(price1:int, price2:int)->str:
    return f"Your total bill is USD {price1 + price2}"

price = total_price(30,40)

print(price) #output: Your total bill is USD 70

# price = total_price('30','40') #output: error: Argument 1 to "total_price" 
# has incompatible type "str"; expected "int"