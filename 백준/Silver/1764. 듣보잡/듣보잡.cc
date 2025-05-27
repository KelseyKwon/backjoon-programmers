/*
듣도 못한 사람 : N
보도 못한 사람 : M

이름 길이는 20 이하
N, M <= 500000 자연수.

각 명단에는 중복이 없다. 교집합이 답. 
*/

/*
시간 초과
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

vector<string> not_seen;
vector<string> not_heard;

bool isInNotHeard(string s) {
  for (int i=0; i<not_heard.size(); i++) {
    if (s == not_heard[i]) {
      return true;
    }
  }
  return false;
}

int main() {
  int N, M;
  cin >> N >> M;

  vector<string> answer;

  for (int i=0; i<N; i++) {
    string s;
    cin >> s;
    not_seen.push_back(s);
  }

  for (int i=0; i<M; i++) {
    string s;
    cin >> s;
    not_heard.push_back(s);
  }

  for (int i=0; i<N; i++) {
    if (isInNotHeard(not_seen[i])) {
      answer.push_back(not_seen[i]);
    }
  }

  sort(answer.begin(), answer.end());
  cout << answer.size() << endl;
  for (string s : answer) {
    cout << s << endl;
  }
}
  */

#include <unordered_map>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int N, M;

  cin >> N >> M;
  unordered_map<string, int> nums; 

  for (int i=0; i<N; i++) {
    string s;
    cin >> s;
    nums[s]+=1;
  }

  for (int i=0; i<M; i++) {
    string s;
    cin >> s;
    nums[s]+=1;
  }

  int count = 0;
  vector<string> answer;
  for (auto &pair : nums) {
    if (pair.second == 2) {
      count++;
      answer.push_back(pair.first);
    }
  }

  sort(answer.begin(), answer.end());
  cout << count << endl;
  for (int i=0; i<count; i++) {
    cout << answer[i] << endl;
  }
}



