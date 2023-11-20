#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")
greet_programmer()


def greet(name):
    pass
    print(f"Hello, {name}!")
greet("Doe")

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")
greet_with_default("John")

def add(num1, num2):
    pass
    return num1 + num2
result = add(45, 55)
print(result)

def halve(number):
    return number / 2

halved_value = halve(100)
print(halved_value)

