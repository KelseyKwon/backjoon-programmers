def solution(players, m, k):
    answer = 0
    server = [0 for _ in range(len(players) + k)]
    
    for i in range(len(players)):
        if players[i] < m:
            continue
        else:
            needed_server = players[i] // m
            print(needed_server, players[i], i, str(i)+"처음")
            if server[i] >= needed_server:
                continue
            else:
                added_server = needed_server - server[i]
                for j in range(i, i+k):
                    server[j] += added_server
                answer += added_server
    return answer
    