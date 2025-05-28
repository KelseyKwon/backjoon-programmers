/*
수의 개수 N, 합을 구해야 하는 횟수 M
둘째줄에 N
그 다음에 M에 걸쳐서 구간함.
sum[i] = sum[i-1] + nums[i];
누적합을 구하고 -> 구간합은 누적합[i] - 누적합[i-1]
*/

#include <iostream>
#include <vector>

using namespace std;

int N, M;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  cin >> N >> M;
  vector<int> nums(N);
  vector<int> sums(N+1);

  for (int i=0; i<N; i++) {
    cin >> nums[i];
    sums[i+1] = sums[i] + nums[i];
  }

  for (int i=0; i<M; i++) {
    int start, end;
    cin >> start >> end;
    cout << sums[end] - sums[start-1] << '\n';
  }
    
  return 0;

}