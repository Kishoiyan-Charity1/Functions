# Write a function that accepts any number of integers as positional
# arguments and any number of a student's attributes as keyword arguments 
# and prints the result of multiplying all of the integers with a customized 
# greeting based on the keyword arguments. Name the function multiply_and_greet.

def multiply_and_greet(*args, **kwargs):
    multiply=1
    for x in args:
        multiply*=x

    print(multiply)
    keys=kwargs.keys()
    if 'country' in keys:
        print (f"hello {kwargs['name']} from {kwargs['country']}")

    elif'age' in keys:
        year=2022-kwargs['age']
        print(f"hello {kwargs['name']} you were born in {year}")

    elif "name" in keys:
        print (f"hello{kwargs['name']}")

    else:
        print(f"hello me")
