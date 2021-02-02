def solution(data, n):
    remove = []
    for num in data:
        count = data.count(num)
        if count > n and not num in remove:
            remove.append(num)
    for item in remove:
        for i in range(data.count(item)):
            data.remove(item)
    return data