

def sum(*args):
    result=0
    for value in args:
        result+=value

    return result


def average(*args):
    return sum(*args)/len(args)


if __name__=='__main__':
    print('testing maths module {}'.format(__name__))
    print('sum(1,2,3,4)=>{}'.format(sum(1,2,3,4)))
    print('average(1,2,3,4)=>{}'.format(average(1,2,3,4)))
    print('=='*25)





