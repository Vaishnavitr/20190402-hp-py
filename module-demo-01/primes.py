

def is_prime(number):
    if number<2:return False

    for test in range(2,number):
        if number%test==0:
            return False

    return True


def prime_range(min,max=None):
    if max is None:
        min,max=2,min

    primes=[]
    for number in range(min,max):
        if is_prime(number):
            primes.append(number)

    return primes



def test():    
    print('testing primes module {}'.\
        format(__name__))
    test_set={-2:False, 0:True, 1:False, 2:True, 9:True, 17:True}
    errors=0
    for test,expected in test_set.items():
        actual=is_prime(test)
        if actual!=expected:
            errors+=1
            print('error for test case {}. expected "{}" found "{}"'.format(test,expected,actual))
    if errors>0:
        print('{}/{} tests failed'.format(errors,len(test_set)))
    else:
        print('all tests passed')

    print('--'*25)

if __name__=='__main__':
    test() 