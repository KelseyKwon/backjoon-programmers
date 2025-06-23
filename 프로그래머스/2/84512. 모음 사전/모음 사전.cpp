#include <string>
#include <vector>

using namespace std;
int count, answer;
char alphabet[5] = {'A', 'E', 'I', 'O', 'U'};

void dfs(string word, string next) {
    if (next == word) {
        answer = count;
        return;
    }

    if (next.length() >= 5) {
        return;
    }

    for (int i=0; i<5; i++) {
        count += 1;
        dfs(word, next + alphabet[i]);
    }
}

int solution(string word) {
    dfs(word, "");
    return answer;
}