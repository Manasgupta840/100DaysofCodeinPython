def add(*args):
    total_sum = 0
    for n in args:
        total_sum = total_sum + n
    print(total_sum)


add(3, 4, 5)


def calcuate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n += kwargs["multiply"]
    print(n)


calcuate(2, add=3, multiply=5)
