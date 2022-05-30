
from typing import KeysView
from unittest import result


def hello(name,age):
    year=2022-age
    print(f"hello{name} you were born in {year}")

def my_country(country='kenya'):
    return f'my country is {country}'

def greet(name):
    print(f'hello {name}')
    return

def greet2(*names):
    print(names)
    return

def greet3(*names):
    for name in names:
        print(f'hello {names}')

def sum(numbers):
    total=0
    for x in numbers:
        total +=x
        return total

def multiply(numb):
    total=0
    for x in numbers:
        total *=x
        return total
    

def greet_multiples(**kwargs):
    keys= kwargs.keys
    values= kwargs.values
    print(keys)
    print(values)

def greet_multiple2(**kwargs):
    keys=kwargs.keys()
    if "country" in keys:
        return f"hello kwargs['name'] from kwargs ['country']"      

    elif "age" in keys:
        year=2022-kwargs["age"]
        return f"hello kwargs['name'] you are born in {year}"
    
    elif 'name' in keys:
        return f"hello kwargs ['name']"

    else: return f"hello annomimous" 

def sum_and_greet(*args, **kwargs):
    print (args)
    print(kwargs)


# Write a function that accepts any number of integers as positional
# arguments and any number of a student's attributes as keyword arguments 
# and prints the result of multiplying all of the integers with a customized 
# greeting based on the keyword arguments. Name the function multiply_and_greet.



    