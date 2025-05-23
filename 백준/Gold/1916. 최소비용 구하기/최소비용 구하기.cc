/*
graph[1] = { {2, 4}, {3, 2} }
graph[2] = { {3, 5} }
graph[3] = { }

비용이 가장 적은 노드를 빨리 꺼내야 함 -> 우선순위 큐 필요!
priority_queue는 삽입/삭제에 성능이 매우 좋다.

pq.push({0, 시작정점});
while (!pq.empty()) {
    auto [cur_cost, cur_node] = pq.top();
    pq.pop();

    for (auto [next, weight] : graph[cur_node]) {
        if (새 비용 < dist[next]) {
            dist[next] = 새 비용;
            pq.push({새 비용, next});
        }
    }
}

priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
1. 벡터에 담길 자료형 , 2. 벡터, 3. 비교기준준
*/

#include <vector>
#include <iostream>
#include <climits>
#include <queue>

using namespace std;

vector<vector<pair<int, int>>> edge_list;
int N, M;
const int INF = INT_MAX;

vector<int> bellman_ford(int start) {
    vector<int> dist(N+1, INF);
    dist[start] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, start});

    while(!pq.empty()) {
        int cur_cost = pq.top().first;
        int cur_node = pq.top().second;
        pq.pop();

        if (cur_cost > dist[cur_node]) continue;

        for (auto& [next, weight] : edge_list[cur_node]) {
            int new_cost = cur_cost + weight;
            if (new_cost < dist[next]) {
                dist[next] = new_cost;
                pq.push({new_cost, next});
            }
        }
    }
    return dist;
}

int main() {
    cin >> N;
    cin >> M;

    edge_list.resize(N+1);


    for (int i=0; i<M; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edge_list[u].push_back({v, w});
    }

    int start_node, end_node;
    cin >> start_node >> end_node;

    vector<int> dist_list = bellman_ford(start_node);
    cout << dist_list[end_node];
}