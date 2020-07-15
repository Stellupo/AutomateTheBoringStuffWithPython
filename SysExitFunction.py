import sys

while True:
    print('Type exit to exit.')
    answer = input()
    if answer == 'exit':
        sys.exit()
    print('You typed ' + answer + '.')