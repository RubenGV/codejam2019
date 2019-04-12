t = int(input())


def resolve(n):
    num1 = ""

    for i in list(str(n)):
        if i == "4":
            num1 += "1"
        else :
            num1 += "0"

    return '{} {}'.format(int(num1), (n-int(num1)))


for i in range(1, t + 1):
    n = int(input())
    print('Case #{}: {}'.format(i, resolve(n)))
