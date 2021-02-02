from math import log

def solution(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)


def generous(lambs):
    return int(log(lambs + 1)/log(2))


def stingy(lambs):
    a, b = 1, 1
    total = 2
    i = 2
    while True:
        a, b = b, a + b
        total = total + b
        if total > lambs:
            break
        i = i + 1
    return i


if __name__ == '__main__':
    print(solution(10))
