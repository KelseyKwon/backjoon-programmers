#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> nums(N);

  for (int i=0; i<N; i++) {
    cin >> nums[i];
  }
  int answer = 0;
  for (int i=0; i<N; i++) {
    for (int j=(i+1); j<N; j++) {
      for (int k=(j+1); k<N; k++) {
        int cur_num = nums[i] + nums[j] + nums[k];
        if (cur_num <= M) {
          answer = max(answer, cur_num);
        }
      }
    }
  }
  cout << answer << '\n';
  return 0;
}

