/*
항상 A보다 B가 크고, 
A에 취할 수 있는 연산은 2를 곱하거나, 1을 수의 가장 오른쪽에 추가하는 것. 
(즉, A*2 or A*10 + 1)
162에서 올 수 있었던 것 : 81 -> 81은 8 -> 4 -> 2
42에서 올 수 있었던 것 : 21 -> 2 (but 4 > 2이므로 못왔음)
40021 -> 4002 -> 2001 -> 200 -> 100
*/

#include <iostream>
#include <vector>

using namespace std;

int main() {
//  int A, B;
  long long A, B;
  cin >> A >> B;

  int count = 1;
  while (B >= A) {
    if (B == A) {
      cout << count;
      return 0;
    }
    if (B % 2 == 0) {
      count += 1;
      B /= 2;
    } else if (B % 10 == 1) {
      count += 1;
      B /= 10;
    } else {
      break;
    }
  }

  cout << -1;
  return 0;
}