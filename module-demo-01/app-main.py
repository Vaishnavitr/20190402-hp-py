'''
Write a program to

1. take min,max from user
2. find all primes in the range
3. find their sum and average
4. repeat if user needs

'''

from maths import *
from primes import prime_range
import consoleutils as cu

def main():
    run=True
    print('welcome to prime app {}'.format(__name__))
    while run:
        min=cu.read_int('min',2)
        max=cu.read_int('max',100)
        primes=prime_range(min,max)
        tot=sum(*primes)
        avg=average(*primes)
        

        print('primes is range {}-{} are {}'.format(min,max,primes))
        print('sum of all primes is {}'.format(tot))
        print('average of all primes is {}'.format(avg))

        run=cu.read_bool('repeat','yes')



    

main()

