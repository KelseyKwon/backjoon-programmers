#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;

    unordered_map<string, int> dict;
    // char에 정수를 더하면 그 부분만큼 다음 character가 됨.
    for (int i=0; i<26; i++) {
        string key(1, 'A' + i);
        dict[key] = i+1;
    }

    string cur = "";
    for (int i=0; i<msg.length();) {
        cur += msg[i];
        for (int j=i+1; j<msg.length(); j++) {
            if (dict.find(cur + msg[j]) == dict.end()) {
                dict[cur + msg[j]] = dict.size() + 1;
                break;
            } else {
                cur += msg[j];
            }
        }
        answer.push_back(dict[cur]);
        i += cur.length();
        cur = "";
    }
        // 있으면 append.
    return answer;
}