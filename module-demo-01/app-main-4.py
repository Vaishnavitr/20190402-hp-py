import maths as m  # overwrites python average()

#overwrites the maths average() function
def average(x,y):
    print('local average')
    return (x+y)/2

def math():
    print('I am the Matemetician')

def main():
    print(m.average(1,2,3,4))
    print(average(7,2))
    math()


if __name__=='__main__':
    main()


