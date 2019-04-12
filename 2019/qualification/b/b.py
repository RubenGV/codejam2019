t = int(input())


def resolve(size, path):
    solution = ""
    for x in list(path):
        if x == "E":
            solution += "S"
        else:
            solution += "E"

    return solution


for i in range(1, t+1):
    size = int(input())
    path = input()
    print("Case #{}: {}".format(i, resolve(size, path)))
