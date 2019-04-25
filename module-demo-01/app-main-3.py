from maths import *  # overwrites python average()

#overwrites the maths average() function
def average(x,y):
    print('local average')
    return (x+y)/2

def main():
    print(average(1,2,3,4))


if __name__=='__main__':
    main()


