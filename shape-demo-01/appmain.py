import sys
import shapes.circle as circle
import shapes.triangle as triangle


def main(name,args):
    print(triangle.perimeter(3,4,5))
    print(triangle.perimeter(3,4,12))
    print(circle.perimeter(7))
    print(circle.perimeter(-9))



if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])