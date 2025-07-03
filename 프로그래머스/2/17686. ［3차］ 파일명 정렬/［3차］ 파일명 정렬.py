def solution(files):
    answer = []
    parsed = []

    for i, fname in enumerate(files):
      num_start = next(idx for idx, ch in enumerate(fname) if ch.isdigit())
      num_end = num_start
      while num_end < len(fname) and fname[num_end].isdigit() and num_end - num_start < 5:
        num_end += 1
      head = fname[:num_start]
      number = fname[num_start:num_end]
      parsed.append((head, number, i))
    
    parsed.sort(key=lambda x: (x[0].lower(), int(x[1]), x[2]))

    answer = [files[i] for _, _, i in parsed]

      
    return answer