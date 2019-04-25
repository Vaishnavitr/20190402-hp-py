import sys
import ca.calculations.maths as m

def main(name,args):
    total = sum( float(value) for value in args )
    print(total)

if __name__=='__main__':
    main(sys.argv[0],  sys.argv[1:])

