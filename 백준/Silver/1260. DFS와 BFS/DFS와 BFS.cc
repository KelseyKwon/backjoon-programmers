#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<vector<int>> graph;
vector<bool> visited;
vector<int> order;
int N, M, V;

void dfs(int node) {
  visited[node] = true;
  order.push_back(node);
  for (int next : graph[node]) {
    if (!visited[next]) dfs(next);
  }
}

vector<int> getdfs() {
  visited.assign(N+1, false);
  order.clear();
  dfs(V);
  return order;
}

void bfs(int node) {
  queue<int> heap;
  heap.push(node);

  while (!heap.empty()) {
    int node = heap.front();
    heap.pop();

    visited[node] = true;
    order.push_back(node);

    for (int neighbor : graph[node]) {
      if (!visited[neighbor]) {
        heap.push(neighbor);
        visited[neighbor] = true;
      }
    }
  }
}

vector<int> getbfs() {
  visited.assign(N+1, false);
  order.clear();
  bfs(V);
  return order;
}

void printOutVector(vector<int> &results) {
  for (int element : results) {
    cout << element << " ";
  }
}

int main() {
  cin >> N >> M >> V;
  graph.assign(N+1, vector<int>());

  for (int i=0; i<M; i++) {
    int start, end;
    cin >> start >> end;

    graph[start].push_back(end);
    graph[end].push_back(start);
  }

  // 작은 번호 먼저 탐색하기 위해 정렬한다. 
  for (int i=1; i<=N; i++) {
    sort(graph[i].begin(), graph[i].end());
  }

  vector<int> dfs_result = getdfs();
  vector<int> bfs_result = getbfs();


  printOutVector(dfs_result);
  cout << "\n";
  printOutVector(bfs_result);
  
}