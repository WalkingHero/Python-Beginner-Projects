n = input('choose a cap for the fibonacci sequence: ')
int_n = int(n)

x = 0
y = 1

while x < int_n:
    print(x)

    z = x + y
    y = x
    x = z

input('Press enter to close..')
