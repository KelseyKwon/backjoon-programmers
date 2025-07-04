import itertools

def solution(k, dungeons):
    def checked(k, dungeon):
        cur_fatigue = k
        count = 0
        for stage in dungeon:
            if cur_fatigue >= stage[0]:
                cur_fatigue -= stage[1]
                count += 1
            else:
                return count
        return count
    answer = 0
    
    for element in itertools.permutations(dungeons):
        answer = max(answer, checked(k, element))
    
    return answer