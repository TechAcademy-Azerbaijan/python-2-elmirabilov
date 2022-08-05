import datetime
from os.path import exists
import sys

if not exists('sample.txt'):
    with open('sample.txt', 'w') as f:
        f.write('Function name |    worked time    | arguments as list | arguments as dictionary | function result \n')

def logger(f):
    """Write task solution here"""
    def wrapper(*args,**kwargs):
        try:
            result = f(*args,**kwargs)
        except ZeroDivisionError as e:
            result = f'Zerodivisionerror: {e}'
        except ValueError as e:
            result = f'ValueError: {e}'
        except TypeError as e:
            result = f'TypeError: {e}'

        current_time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        with open('sample.txt', 'a') as file:
            if args:
                file.write(f'{f.__name__}       | {current_time} |  {str(args)}      |              |     {result} \n ')
            else:
                file.write(f'{f.__name__}       | {current_time} |           | {str(kwargs)}|       {result} \n ')
               
    return wrapper

@logger
def sum(a,b):
    return a+b
@logger
def divide(a,b):
    return a/b

sum(1,2)
divide(a=4,b=2)
divide(10,0)