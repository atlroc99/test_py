import logging
import json

# basic configuration
# filemode  Specifies the mode to open the file, if filename is specified
#               (if filemode is unspecified, it defaults to 'a').

logging.basicConfig(level=logging.DEBUG, filename='../logs/output.log')


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 200
num_2 = 5

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

subtract_result = subtract(num_1, num_2)
logging.debug('Subtract: {} - {} = {}'.format(num_1, num_2, subtract_result))

division_result = divide(num_1, num_2)
logging.debug('Division: {} / {} = {}'.format(num_1, num_2, division_result))

multiplication_result = multiply(num_1, num_2)
logging.debug('Multiplication: {} x {} = {}'.format(num_1, num_2, multiplication_result))
