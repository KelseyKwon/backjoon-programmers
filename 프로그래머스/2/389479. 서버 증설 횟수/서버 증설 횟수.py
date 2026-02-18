"""
n명 이상, n+1명 미만 -> N대으이 증설된 서버가 운영중이여야 함!

k시간 운영, 그 이후에는 반납. 

최소! 몇번 서버 증설?

len(players) = 24
m, k

m = k = 1일때?

운영중인 서버의 대수는 최소 players[i] // m 개여야 한다. 

server = []



"""
def solution(players, m, k):
    answer = 0
    
    n = len(players)
    server = [0 for _ in range(24)]
    print(server)
    
    for i in range(n):
        cur_server = players[i] // m
        if (players[i] == 0):
            continue
        else:
            # print(players[i], server)
            if server[i] < cur_server:
                diff = cur_server - server[i]
                answer += diff
                # for i in range(i, i+k):
                for j in range(i, min(i+k, 24)):
                    # if i+k >= len(server):
                    #     break
                    # server[i] = max(server[i], cur_server)
                    server[j] += diff
    return answer