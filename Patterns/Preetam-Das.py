n = 16 # change the value to chenge the size
for i in range(0, n):
    print('*'*(i+1),end='')
    print(' '*(n - i),end='')
    print(' '*(n - i - 1),end='')
    print('*'*(i + 1),end='')
    print('*'*(i),end='')
    print(' '*(n - i),end='')
    print(' '*(n - i - 1),end='')
    print('*'*(i + 1),end='')
    print()