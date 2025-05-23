/*
topological sort : directed acyclic graph에서만 사용 가능.
자신을 향한 화살표 개수를 진입 차수로 정의해 진행한다. (진입 차수 : 자신을 향한 화살표의 개수)

만약에 진입차수 = 0, 선행 작업이 필요없는 바로 할 수 있는 일. 따라서 이게 0인 것을 해결하고 관련된 작업의 진입차수를 1씩 낮춘다!

큐를 이용해서 구현. 0인 것을 전부 큐에 넣고 -> 팝하면서 -> 연결되어 있는 진입차수를 줄인다. 

시간 복잡도 : O(V + E);
*/

/*
#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> nodes;
vector<vector<int>> adj;
vector<int> answer;

int main() {
    cin >> N >> M;
    nodes.resize(N+1);
    for (int i=0; i<M; i++) {
        int u, e;
        cin >> u >> e;

        adj[u].push_back(e);
        nodes[e]++;
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    int start = 0;
    for (int i=1; i<nodes.size(); i++) {
        if (nodes[i] == 0) {
            start = i;
            break;
        }
    }

    pq.push({nodes[start], start});

    while (!pq.empty()) {
        int cur = pq.top().second;
        answer.push_back(cur);
        pq.pop();

        for (int neighbor : adj[cur]) {
            nodes[neighbor]--;
            pq.push({nodes[neighbor], neighbor});
        }
    }

    for (int i: answer) {
        cout << i << " ";
    }
}

위에서의 치명적인 실수 : 진입차수 0이 아닌 노드도 push한다. 따라서 진입차수가 0이 되었을때만
큐에 넣는 것이 핵심! 
*/

#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> nodes;
vector<vector<int>> adj;
vector<int> answer;

int main() {
    cin >> N >> M;
    nodes.resize(N+1);
    adj.resize(N+1);
    for (int i=0; i<M; i++) {
        int u, e;
        cin >> u >> e;

        adj[u].push_back(e);
        nodes[e]++;
    }

    priority_queue<int, vector<int>, greater<>> pq;
    for (int i=1; i<nodes.size(); i++) {
        if (nodes[i] == 0) {
            pq.push(i);
        }
    }

    while (!pq.empty()) {
        int cur = pq.top();
        answer.push_back(cur);
        pq.pop();

        for (int neighbor : adj[cur]) {
            nodes[neighbor]--;
            if (nodes[neighbor] == 0)
                pq.push(neighbor);
        }
    }

    for (int i: answer) {
        cout << i << " ";
    }
}