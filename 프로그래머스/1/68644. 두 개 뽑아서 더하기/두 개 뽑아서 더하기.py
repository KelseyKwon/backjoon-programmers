def solution(numbers):
    answer = set()
    numbers.sort()
    
    for i in range(len(numbers)):
      for j in range(i+1, len(numbers)):
        answer.add(numbers[i] + numbers[j])

    # return answer
    return sorted(answer)