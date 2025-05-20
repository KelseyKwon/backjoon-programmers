// 코스 길이 : 4~12
// 지형 여러개
// 개인 성적 매기고 -> 팀의 점수
// 한 팀 : 여섯명의 선수, 팀 점수는 상위 네 명의 주자의 점수를 합한다.
// 점수 : 자격을 갖춘 팀의 주자들에게만 주어지고 (각 팀은 6명이여야 함), 결승점을 통과한 순서대로 점수를 받음.
// A (1, 4, 6, 7, 9, 12)
// B <6 --> n/a
// C : {2, 3, 5, 8, 10, 11}
// D <6 -> n/a
// A == B, A.5 < C.5이므로 A팀이 우승한다.

#include <iostream>
#include <vector>
#include <unordered_map>
#include <numeric>
#include <climits>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int i=0; i<T; i++) {
    int D;
    cin >> D;

    unordered_map<int, int> team_count;
    // 팀 정보, 점수가 나와있음.
    vector<int> record(D);
    for (int i=0; i<D; i++) {
      cin >> record[i];
      ++team_count[record[i]];
    }

    unordered_map<int, vector<int>> score_map;

    int score = 1;
    for (int i=0; i<record.size(); i++) {
      if (team_count[record[i]] != 6) {
        continue;
      } else {
        score_map[record[i]].push_back(score);
        score += 1;
      }
    }

    int min_score = INT_MAX;
    int winning_team = 0;

    for (auto& kv : score_map) {
      int cur_score = 0;
      for (int i=0; i<4; i++) {
        cur_score += kv.second[i];
      }
      if (cur_score < min_score) {
        winning_team = kv.first;
        min_score = cur_score;
      } else if (cur_score == min_score) {
        if (score_map[winning_team].at(4) > score_map[kv.first].at(4)) {
          winning_team = kv.first;
          min_score = cur_score;
        }
      }
  }
  cout << winning_team << "\n";
}
return 0;
}