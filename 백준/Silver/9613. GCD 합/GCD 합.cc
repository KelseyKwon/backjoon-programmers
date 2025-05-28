/*
10
// 일단 입력을 받고,
쌍을 구해.
그리고 gcd 함수를 호출해서 
*/

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
long long sum;

/*
int gcd(int a, int b) {
  int flag = min(a, b);
  for (int i=flag; i>=1; i--) {
    if (a % i == 0 && b % i == 0) {
      return i;
    }
  }
}
  */

int gcd(int a, int b) {
  while (b!=0) {
    int temp = a % b;
    a = b;
    b = temp;
  }
  return a;
}

int main() {
  int t;
  cin >> t;
  for (int i=0; i<t; i++) {
    int n;
    sum = 0;
    cin >> n;
    vector<int> nums(n);

    for (int i=0; i<n; i++) {
      cin >> nums[i];
    }

    for (int i=0; i<nums.size()-1; i++) {
      for (int j=i+1; j<nums.size(); j++) {
        sum += gcd(nums[i], nums[j]);
      }
    }

    cout << sum << '\n';
  }
}