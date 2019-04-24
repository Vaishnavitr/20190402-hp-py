'''
Let us test one of the modules -- consoleutils
'''
import consoleutils

def main():
    print(type(consoleutils))
    print(dir(consoleutils))

    answer=True
    while answer:
        name=consoleutils.read_string('name')
        print('hello {}, welcome to python'.format(name))
        answer=consoleutils.read_bool('want to continue', default='y', suffix='?')

main()

