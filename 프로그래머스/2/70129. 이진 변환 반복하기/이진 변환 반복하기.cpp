#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer(2); // {회차, 제거한 0의 개수}
    int zero_count = 0;
    int round_count = 0;

    while (s != "10") {
      string temp = "";
      round_count += 1;
      // 0 제거
      for (char c : s) {
        if (c == '0') {
          zero_count += 1;
        } else {
          temp += c;
        }
      }

      // 2진법으로 변환
      int cal_num = temp.size();
      vector<int> results;

      while (cal_num / 2 != 0) {
        results.push_back(cal_num % 2);
        cal_num /= 2;
      } 
      
      s = "";
      for (int i=results.size()-1; i>=0; i--) {
        s += results[i];
      }
  
    }
    round_count += 1;
    zero_count += 1;
    answer[0] = round_count;
    answer[1] = zero_count;

    return answer;
}
    */

    #include <string>
    #include <vector>
    
    using namespace std;
    
    vector<int> solution(string s) {
        vector<int> answer(2); // {횟수, 제거한 0의 개수}
        int zero_count = 0, round_count = 0;
    
        while (s != "1") {
            string temp = "";
            for (char c : s) {
                if (c == '0') zero_count++;
                else temp += c;
            }
    
            int cal_num = temp.size();
            s = "";
            while (cal_num > 0) {
                s = char((cal_num % 2) + '0') + s;
                cal_num /= 2;
            }
            round_count++;
        }
    
        answer[0] = round_count;
        answer[1] = zero_count;
        return answer;
    }
    
