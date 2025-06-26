"""
def all_shortest(strings):
  min_len = min(len(s) for s in strings)
  return [s for s in strings if len(s) == min_len]

def solution(phone_book):
    answer = True

    candidate = set(all_shortest(phone_book))
    N = min(len(s) for s in phone_book)

    for i in phone_book:
      if len(i) > N and i[0:N] in candidate:
        return True
    else:
      return False
"""

def solution(phone_book):
  phone_book.sort()

  for i in range(len(phone_book) - 1):
    if phone_book[i+1].startswith(phone_book[i]):
      return False

  return True