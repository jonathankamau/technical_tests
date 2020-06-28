#!/bin/python

import math
import os
import random
import re
import sys

def consumer():
    while True:
        x = yield
        print(x)

def producer(n):
    for _ in range(n):
        x = int(input())
        yield x


# Complete the 'rooter', 'squarer', and 'accumulator' function below.

def rooter():
    # Write your code here
    number = yield
    while True:
        number = yield int(math.floor(math.sqrt(number)))

def squarer():
    # Write your code here
    number = yield
    while True:
        number = yield number * number

def accumulator():
    # Write your code here
    number = yield
    while True:
        number = number + (yield number) 
    

def pipeline(prod, workers, cons):
    for num in prod:
        for i, w in enumerate(workers):
            num = w.send(num)
        cons.send(num)
    for worker in workers:
        worker.close()
    cons.close()


if __name__ == '__main__':
    order = input().strip()
    
    n = int(input())

    prod = producer(n)

    cons = consumer()
    next(cons)
    
    root = rooter()
    next(root)

    accumulate = accumulator()
    next(accumulate)

    square = squarer()
    next(square)

    pipeline(prod, eval(order), cons)
