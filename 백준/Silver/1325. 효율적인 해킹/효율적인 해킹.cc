/*
시간 초과...
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int N, M;

unordered_map<int, vector<int>> graph;

// dfs 주요 핵심 : 재귀호출할게 없으면 그 순간 cnt 반환 시작 -> 1 -> 2 -> 3 으로 감.
int dfs(int index, vector<bool> &visited) {
    visited[index] = true;
    int cnt = 1;
    for (int next : graph[index]) {
        if (!visited[next]) {
            cnt += dfs(next, visited);
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    cin >> N >> M;
    
    while(M--) {
        int to, from;
        cin >> to >> from;
        graph[from].push_back(to);
    }
    vector<int> answers(N+1);
    for (int i=1; i<=N; i++) {
        vector<bool> visited(N+1, false);
        answers[i] = dfs(i, visited);
    }

    vector<int> results;
    int max = *max_element(answers.begin(), answers.end());
    for (int i=1; i<=N; i++) {
        if (answers[i] == max) {
            cout << i << " ";
        }
    }

    return 0;
}
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <queue>
using namespace std;

int N, M;
unordered_map<int, vector<int>> graph;

// dfs 주요 핵심 : 재귀호출할게 없으면 그 순간 cnt 반환 시작 -> 1 -> 2 -> 3 으로 감.
int dfs(int index) {
    vector<bool> visited(N+1);
    queue<int> q;
    q.push(index);
    visited[index] = true;
    int cnt = 1;

    while(!q.empty()) {
        int cur = q.front(); q.pop();
        for (int i: graph[cur]) {
            if (!visited[i]) {
                visited[i] = true;
                q.push(i);
                cnt++;
            }
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    cin >> N >> M;
    
    while(M--) {
        int to, from;
        cin >> to >> from;
        graph[from].push_back(to);
    }
    vector<int> answers(N+1);
    int max_count = 0;
    for (int i=1; i<=N; i++) {
        answers[i] = dfs(i);
        max_count = max(max_count, answers[i]);
    }

    for (int i=1; i<=N; i++) {
        if (answers[i] == max_count) {
            cout << i << " ";
        }
    }

    return 0;
}