def solution(start, length):
    ans = list_gen(start, length)
    return ans


def list_gen(start, length):
    answer = 0
    for j in range(0, length):
        answer ^= xor_line((length*j)+start, (length*j) + start + length - j -1)
    return answer
       

def xor_line(a, b):
    if a % 2 == 0:
        xor_rotation = [ b, 1, b + 1, 0 ]
    else:
        xor_rotation = [ a, a ^ b, a - 1, (a - 1) ^ b ]
    return xor_rotation[ (b - a) % 4 ]


if __name__ == "__main__":
    print(solution(0, 3))