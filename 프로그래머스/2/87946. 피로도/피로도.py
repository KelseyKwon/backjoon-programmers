from itertools import permutations

def search(list, k):
    count = 0
    for i in list:
        if (k >= i[0]):
            k -= i[1]
            count += 1
        else:
            return count
    return count


def solution(k, dungeons):
    answer = -1

    for list in permutations(dungeons, len(dungeons)):
        answer = max(answer, search(list, k))

    return answer