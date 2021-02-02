def solution(version_nums):
    for f in range(len(version_nums)):
        version_nums[f] = version_nums[f].split(".")

    for i in range(0, len(version_nums) - 1):
        for j in range(0, len(version_nums) - 1 - i):
            if higher_lower(version_nums[ j + 1 ], version_nums[ j ]):
                version_nums[ j ], version_nums[ j + 1 ] = version_nums[ j + 1 ], version_nums[ j ]
    
    for k in range(len(version_nums)):
        version_nums[k] = ".".join(version_nums[k])
    
    return version_nums

def higher_lower(a, b):
    if a == b:
        return True
    if int(a[0]) == int(b[0]):
        if len(a) != 1 and len(b) == 1:
            return False
        elif len(a) == 1 and len(b) != 1:
            return True
        else:
            if int(a[1]) == int(b[1]):
                if len(a) != 2 and len(b) == 2:
                    return False
                elif len(a) == 2 and len(b) != 2:
                    return True
                else:
                    if int(a[1]) < int(b[1]):
                        return True
                    else:
                        if int(a[2]) < int(b[2]):
                            return True
                        else:
                            return False
            elif int(a[1]) < int(b[1]):
                return True
            else:
                return False
    elif int(a[0]) < int(b[0]):
        return True
    else:
        return False

if __name__ == "__main__":
    lol = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]


    print(solution(lol))