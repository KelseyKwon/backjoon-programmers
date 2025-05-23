/*
왜 graph에 weight을 먼저 넣어? -> priority queue의 비교 기준이
tuple 또는 pair의 첫번째 값이기 때문!

Prim / Dijkstra / Kruskal 등 가중치 기반 선택 알고리즘에서는 항상:
pair<int, int> = {cost, vertex}
*/

#include <bits/stdc++.h>

using namespace std;
using pr = pair<int, int>;
using tp = tuple<int, int, int>;

int V, E;
vector<vector<pr>> graph;
bool isMST[10001]; //각 노드마다 Minimum spanning tree에 포함되어있는지 여부

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> V >> E;
    graph.resize(V+1);

    for (int i=1; i<=E; i++) {
        int start, end, weight;
        cin >> start >> end >> weight;
        graph[start].push_back({weight, end});
        graph[end].push_back({weight, start});
    }

    int start = 1, cnt = 0, ans = 0;
    isMST[start] = true; //일단 1번 노드는 방문했다고 함. 
    priority_queue<tp, vector<tp>, greater<tp>> pq;

    // 인접리스트 start번에 담긴 모든 pair을 검사
    for (auto nb : graph[start]) {
        pq.push({nb.first, start, nb.second});
    }
    while (cnt < V - 1) {
        int cost, from, to;
        tie(cost, from, to) = pq.top(); pq.pop();

        if (isMST[to]) continue;

        isMST[to] = true;
        ans += cost;
        cnt++;

        for (auto nb : graph[to]) {
            if (!isMST[nb.second]) {
                pq.push({nb.first, to, nb.second});
            }
        }
    }

    cout << ans << '\n';
    return 0;
}