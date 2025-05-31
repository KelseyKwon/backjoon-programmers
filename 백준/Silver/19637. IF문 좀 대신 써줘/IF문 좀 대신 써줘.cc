/*
10000이하 : WEAK 10000~100000 : NORMAL, 100000초과 : STRONG
1초

*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
	cin.tie(0), cout.tie(0);
  
  int N, M;
  cin >> N >> M;
  vector<pair<string, int>> info(N);

  for (int i=0; i<N; i++) {
    cin >> info[i].first >> info[i].second;
  }

  int num;
  for (int i=0; i<M; i++) {
    cin >> num;

    int left = 0, right = N-1;
    int res = N-1; // 마지막 칭호의 인덱스로 기본 설정.

    while (left <= right) { //왼쪽 포인터가 더 작을때까지
      int mid = (left + right) / 2;
      if (num <= info[mid].second) {
        res = mid;
        right = mid-1;
      } else {
        left = mid + 1;
      }
    }
    cout << info[res].first << '\n';
  }
  return 0;
}