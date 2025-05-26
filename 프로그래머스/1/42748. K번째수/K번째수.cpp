#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int sort(int i, int j, int k) {

}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for (auto& rows : commands) {
      int i = rows[0];
      int j = rows[1];
      int k = rows[2];
      vector<int> sub(array.begin() + (i-1), array.begin() + j);
      sort(sub.begin(), sub.end());
      answer.push_back(sub[k-1]);

    }

    return answer;
}