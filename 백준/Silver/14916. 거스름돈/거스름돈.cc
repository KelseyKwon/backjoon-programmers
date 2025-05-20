/*
// 아래 코드는 12와 같은 경우에 6을 출력해 실제 min 값을 반환하지 못한다.
// 홀수 이면서 5의 배수 ; N / 5
// 짝
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int N, result;
  cin >> N;

  if (N < 5) {
    if (N == 1 || N == 3) result = -1;
    if (N == 2) result = 1;
    if (N == 4) result = 2;
  }

  if (N >= 5) {
    vector<int> nums(N+1);
    nums[2] = 1;
    nums[5] = 1;

    for (int i=0; i<=N; i++) {
      nums[i] = -1;

      if (nums[i-2] != -1) {
        nums[i] = nums[i-2] + 1;
      }

      if (i % 5 == 0) {
        nums[i] = i / 5;
      }
    }
    result = nums[N];
  }

  cout << result;

}

*/

#include <iostream>

using namespace std;

int main() {
  int N;
  cin >> N;
  int count = 0;

  while (N>=0) {
    if (N%5 == 0) {
      count += N / 5;
      cout << count;
      return 0;
    }
    N -= 2;
    count += 1;
  }

  cout << -1;
}