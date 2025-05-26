#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const string &a, const string &b) {
  return a + b > b + a;
}

string solution(vector<int> numbers) {
    vector<string> answers;
    string answer = "";
    answers.push_back(to_string(numbers[0]));

    for (int i=1; i<numbers.size(); i++) {
      string temp = to_string(numbers[i]);
      answers.push_back(temp);
    }

      // 3, 30, 34이런식으로 배치되어 있으면,
      // 330, 34330이런식으로 정렬됨.
      sort(answers.begin(), answers.end(), cmp);
    for (auto &temp : answers) {
      answer += temp;
    }

    // 주의 ! 원소가 0이상 1000이하 이므로 0인 원소가 100개 있을 수도 있다.
    // 이럴떄 0을 100개 출력하면 안되므로 아래와 같이 작성.
    if (answer[0] == '0') {
      return "0";
    }

    return answer;
}