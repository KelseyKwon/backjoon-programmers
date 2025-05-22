/*
일단 vector alphabet에 a, n, t, a, c을 넣어
그 다음 글자에서 좌우 빼고 가운데 알파벳을 읽어.
그리고 벡터에 존재하는게 아니면 넣어.
벡터의 길이가 K가 될때까지 해. 

그리고 해당 글자로 각 글자에 해당 알파벳이 존재하는지 확인해.
다 존재하면 -> +1
*/

/*
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int N, K;
unordered_set<char> alphabet = {'a', 'n', 't', 'i', 'c'};
vector<string> sub_word;

int main() {
  cin >> N >> K;
  sub_word.resize(N, "");
  int result = 0;

  if (K < 5) {
    cout << result;
    return;
  }

  for (int i=0; i<N; i++) {
    string word;
    cin >> word;
    word.substr(4, word.length() - 8);

    while (alphabet.size() < K) {
    for (int i=0; i<word.length(); i++) {
      alphabet.insert(word[i]);
    }
  }
  }

}

특정한 char가 있는지 없는지 확인하는 법은
unordered_set에 일일이 추가하면 나중에 비교하기 어려움.
차라리 각 알파벳을 int로 변환해서 bool [] 배열을 만든다!

그리고 나는 기존에 각 단어마다 해당 char가 특정 배열에 있는지 확인하고,
없으면 K++ 하고, 그 상태로 또 다음 단어를 돌면서 읽을 수 있는지 확인하고 싶었지만
for문을 어떻게 써야되는지 몰라서 난감했음.
그냥 애초에 a, n, t, i, c을 true로 저장하고, 모든 알파벳마다 true로 저장한다.
  */

#include <iostream>
#include <vector>

using namespace std;

vector<string> parsed_word;
bool alphabet[26];
int N, K, result = 0;

void dfs(int depth, int k) {
  if (k > K) {
    return;
  }

  int count = 0;

  for (int i=0; i<N; i++) {
    bool tf = true;
    for (int j=0; j<parsed_word[i].length();j++) {
      if (alphabet[parsed_word[i][j] - 'a']) continue;
      tf = false;
      break;
    }
    if (tf) count++;
  }

  if (k == K) {
    result = max(result, count);
    return;
  }

  for (int i=depth; i<26; i++) {
    if (alphabet[i]) continue;
    alphabet[i] = true;
    dfs(i, k+1);
    alphabet[i] = false;
  }
}

int main() {
  cin >> N >> K;

  for (int i=0; i<N; i++) {
    string str;
    cin >> str;
    parsed_word.push_back(str.substr(4, str.length()-8));
  }

  if (K < 5) {
    cout << 0;
    return 0;
  }

  alphabet['a' - 'a'] = true; 
  alphabet['n' - 'a'] = true; 
  alphabet['t' - 'a'] = true; 
  alphabet['i' - 'a'] = true; 
  alphabet['c' - 'a'] = true;

  dfs(0, 5);

  cout << result;
}