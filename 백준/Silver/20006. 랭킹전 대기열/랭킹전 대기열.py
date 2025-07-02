"""
입장 가능 방 x : 새로운 방 생성하고 입장시킴 (처음 입장 플레이어 기준 -10 ~+10)
입장 가능 방 o : 입장시킨 후 방의 정원이 모두 찰 때까지 대기시킴

여러개면 먼저 생성된 방에 입장
방의 정원이 모두 차면 게임 시작. 

플레이어 수 : p, 플레이어 닉네임 : n, 플레이어 레벨 : l, 정원 : m

입장 가능 : 제한이 안차고, 레벨이 조건에 맞으면.
아니면 : 새로운 방 생성.

방의 개수는 최대 10개.

"""
# import sys

# input = sys.stdin.readline

# def inRange(level, room_number):
#     return room[room_number][0].values() >= level - 10 and room[room_number][0].values() <= level + 10

# p, m = input().split()
# info = [{} for _ in range(p)]
# for i in range(p):
#     l, n = input().split()
#     info[i][n] = l

# room = [[] for _ in range(p)]
# room_number = 0
# room[room_number].append(info[0])

# for i in range(len(info)):
#     # 방에 사람이 다 찼을때
#     if (len(room[room_number]) == m):
#         room_number+=1
#         room[room_number].append(info[i])
    
#     # 방에 사람이 다 차지 않았고, 레벨도 범위 안에 있을때
#     if (room_people_count < m and inRange(info[i].values, room_number)):
#         room[room_number].append(info[i])
#         room_people_count += 1

import sys

input = sys.stdin.readline

def solution():
    p, m = map(int, input().split())
    rooms = []

    for _ in range(p):
        l, n = input().split()
        # 그냥 input().split()만 하면 char이므로
        # 반드시 int로 형변환을 해줘야 함!
        l = int(l)

        # 매 dictionary마다 matched = False로 초기화해줘야함.
        matched = False

        for room in rooms:
            if len(room['players']) < m and abs(room['base'] - l) <= 10:
                room['players'].append((l, n))
                matched = True
                break # 이 for문만 나옴. 
        if not matched:
            rooms.append({
                'base' : l,
                'players': [(l, n)]
            })

    for room in rooms:
        if len(room['players']) == m:
            print("Started!")
        else:
            print("Waiting!")
        
        for lvl, name in sorted(room['players'], key = lambda x: x[1]):
            print(lvl, name)


if __name__ == "__main__":
    solution()