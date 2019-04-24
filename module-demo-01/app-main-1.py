'''
Write a program to

1. take min,max from user
2. find all primes in the range
3. find their sum and average
4. repeat if user needs

'''

import maths
import primes
import consoleutils

def main():
    run=True
    while run:
        min=consoleutils.read_int('min',2)
        max=consoleutils.read_int('max',100)
        primelist=primes.prime_range(min,max)
        tot=maths.sum(*primelist)
        avg=maths.average(*primelist)

        print('primes is range {}-{} are {}'.format(min,max,primelist))
        print('sum of all primes is {}'.format(tot))
        print('average of all primes is {}'.format(avg))

        run=consoleutils.read_bool('repeat','yes')



    

main()

