def solution(sizes):
    max_list = []
    min_list = []
    
    for i, j in sizes:
        if i >= j:
            max_list.append(i)
            min_list.append(j)
        else:
            max_list.append(j)
            min_list.append(i)
    
    return max(max_list) * max(min_list)