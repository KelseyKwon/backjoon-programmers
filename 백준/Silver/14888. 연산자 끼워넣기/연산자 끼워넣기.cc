// 5! / 2]
// 수의 개수 >= 2, <= 11
// + - * /
// 1 2 3 4 5 6 [+ + - * /] -> 6개
// 3 4 5 [+ *]

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int N;
vector<int> nums;
vector<int> operation;

int main() {
  cin >> N;
  nums.resize(N, 0);

  for (int i=0; i<N; i++) {
    cin >> nums[i];
  }
// 0 0 1 2 3
  for (int i=0; i<4; i++) {
    int count;
    cin >> count;

      for (int j=0; j<count; j++) {
        operation.push_back(i);
      } 
  }

  int min_num = INT_MAX; int max_num = INT_MIN; 

  do {
    int temp = nums[0];
    for (int i=1; i<nums.size(); i++) {
      int next = nums[i];
      if (operation[i-1] == 0) {
        temp +=  nums[i];
      } else if (operation[i-1] ==1) {
        temp -= nums[i];
      } else if (operation[i-1] == 2) {
        temp *= nums[i];
      } else {
        if (temp < 0) temp = -(-temp / next);
        else temp /= next;
      }
    }

    min_num = min(min_num, temp);
    max_num = max(max_num, temp);
  } while (next_permutation(operation.begin(), operation.end()));

  cout << max_num << '\n' << min_num;

}