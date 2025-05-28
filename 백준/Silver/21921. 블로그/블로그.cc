/*
시작한 기간 숫자 N, 구간 숫자 X
N : 0~250000
X : 0~8000
5-2+1 = 4개
7-5+1 = 3개
N-X + 1만큼. 
0 1 2 3
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N, X;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> X;
  vector<int> nums(N);
  vector<int> sums(N-X+1);

  for (int i=0; i<N; i++) {
    cin >> nums[i];
  }

  // 1 1 1 1 1 5 1
  // 1 1 1 1 1 -> 1 1 1 1 5 (1을 빼고 5를 넣기) -> 1 1 1 5 1
  // 첫번째면 다 더해. 그 다음에는 그 전의 sum에서 nums의 첫번째를 빼고 현재 i번째를 더해.
  int sum = 0;
  for (int i=0; i<=N-X; i++) {
    if (i == 0) {
      for (int j=0; j<X; j++) {
        sum += nums[j];
  //      sums[i] = sum;
      }
        sums[i] = sum;
    } else {
      sums[i] = (sums[i-1] - nums[i-1]) + nums[i + X - 1];
    }
  }

  int max_num = *max_element(sums.begin(), sums.end());
  if (max_num == 0) {
    cout << "SAD";
    return 0;
  }
  int count_max_num = count(sums.begin(), sums.end(), max_num);
  cout << max_num << '\n' << count_max_num;

}