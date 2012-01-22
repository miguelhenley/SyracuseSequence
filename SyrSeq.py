__author__ = 'Henley'

def isEven(value):
    return value % 2 == 0;

def get_sequence_size(value):
    elemento = value
    size = 0

    while True:
        size = size + 1

        if (elemento == 1):
            break;

        if isEven(elemento):
            elemento = int(elemento / 2)
        else:
            elemento = 3 * elemento + 1

    return size


def print_sequence(value):
    elemento = value

    while True:
        if (elemento == 1):
            break;

        if isEven(elemento):
            elemento = int(elemento / 2)
        else:
            elemento = 3 * elemento + 1

        print elemento



size = 0
numero = 0

for x in range(25, 26):
    size_seq = get_sequence_size(x)

    if size_seq > size:
        size = size_seq
        numero = x


print numero, size
print_sequence(numero)

