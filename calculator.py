from multiprocessing.connection import answer_challenge


def add(a,b):
    answer = a+b
    return answer

def multiply(a,b):
    answer = a*b
    return answer

def division(a,b):
    answer = a/b
    return answer

def modulus(a,b):
    answer = a%b
    return answer

def exponent(a,b):
    answer = a**b
    return answer

def divide_int(a,b):
    answer = a/b
    return answer

def subtract(a,b):
    answer = a-b
    return answer
    
def cube(a):
    answer = a*a*a
    return answer  

def square(a):
    answer = a*a
    return answer   