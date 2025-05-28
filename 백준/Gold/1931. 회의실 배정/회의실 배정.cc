/*
N개의 회의
N개동안, 시자가 시간 & 끝나는 시간 존재. 
동시에 사용할 수 있는 최대 회의 개수
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const pair<int, int> &a, const pair<int, int> &b) {
  if (a.second == b.second) {
    return (a.first < b.first);
  } else {
    return (a.second < b.second);
  }
}

int main() {
  int N;
  cin >> N;

  vector<pair<int, int>> nums;
  vector<int> answer;

  for (int i=0; i<N; i++) {
    int u, v;
    cin >> u >> v;
    nums.push_back({u, v});
  }

  sort(nums.begin(), nums.end(), compare);
  int count = 1;
  int end = nums[0].second;

  for (int i=1; i<nums.size(); i++) {
    // 끝나는 것과 동시에 시작할 수 있다.
    if (nums[i].first >= end) {
      end = nums[i].second;
      count += 1;
    }
  }

  cout << count;
  
}