import sys

input = sys.stdin.readline

N = input()


def sol():
    a = [0] * 4 + [int(N[i]) for i in range(len(N) -1, -1, -1)]
    b = [int(N[i]) for i in range(len(N) -1, -1, -1)] + [0] * 4

    result = []
    r = 0
    for i in range(len(a)):
        if a[i] + b[i] + r == 3:
            r = 1
            result.append(1)
        elif a[i] + b[i] + r == 2:
            r = 1
            result.append(0)
        elif a[i] + b[i] + r == 1:
            r = 0
            result.append(1)
        else:
            r = 0
            result.append(0)
    
    if r == 1:
        result.append(1)
    
    result.reverse()
    
    print(''.join(map(str, result)))


sol()


# 10001

# 100110000
# 000010011

# 101000011