// 아래 풀이 : 값들을 입력을 받고, 현재 그룹에 둘 중에 하나 값이 있느면
// 추가하고 아니면 index ++ 해서 새로운 그룹으로 배정함.
// --> 1 -> 2, 2 -> 3이면 1 -> 3 임을 적용하기 위해...
// 이 로직은 시작 정점을 visited로 찍고, 계속 탐색하는 방법이 더 효율적...

// #include <iostream>
// #include <unordered_map>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int main()
// {
//   int N, pair_num;
//   // bfs로 찾기.
//   cin >> N >> pair_num;

//   int count = 0;
//   unordered_map<int, vector<int>> nums;

//   int a, b;
//   cin >> a >> b;
//   nums[0].push_back(a); nums[0].push_back(b);

//   for (int i = 0; i < (pair_num-1); i++)
//   {
//     int first_node, second_node;
//     cin >> first_node >> second_node;
//     auto it1 = find(nums[count].begin(), nums[count].end(), first_node);
//     auto it2 = find(nums[count].begin(), nums[count].end(), second_node);

//     if (it1 != nums[count].end() && it2 != nums[count].end()) {
//       continue;
//     }
//     if (it1 != nums[count].end()) {
//       nums[count].push_back(second_node);
//       continue;
//     }
//     if (it2 != nums[count].end()) {
//       nums[count].push_back(first_node);
//       continue;
//     }
//     else {
//       count += 1;
//       nums[count].push_back(first_node);
//       nums[count].push_back(second_node);
//     }
//   }

//   for (auto &pairs : nums) {
//     if (find(pairs.second.begin(), pairs.second.end(), 1) != pairs.second.end()) {
//       cout << pairs.second.size()-1;
//       break;
//     }
//   }

// }

#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<vector<int>> graph;
vector<bool> visited;
int infected_count = 0;

void dfs(int u) {
    visited[u] = true;
    for (int v : graph[u]) {
        if (!visited[v]) {
            infected_count++;
            dfs(v);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    graph.assign(N + 1, vector<int>());
    visited.assign(N + 1, false);

    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    dfs(1);

    cout << infected_count << '\n';
    return 0;
}