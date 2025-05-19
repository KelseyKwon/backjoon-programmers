#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool WithInRange(int x, int y) {
    return (x >= 0 && x < 100 && y >= 0 && y < 100);
}

int main() {
    int test_case;
    cin >> test_case;

    vector<vector<int>> graph(100, vector<int>(100));

    for (int i = 0; i < test_case; i++) {
        int start_x, start_y;
        cin >> start_x >> start_y;

        for (int x = start_x; x < start_x + 10; x++) {
            for (int y = start_y; y < start_y + 10; y++) {
                if (WithInRange(x, y)) {
                    graph[x][y] = 1;
                }
            }
        }
    }

    int count_one = 0;
    for (const auto& row : graph) {
        count_one += count(row.begin(), row.end(), 1);
    }

    cout << count_one << '\n';
    return 0;
}
