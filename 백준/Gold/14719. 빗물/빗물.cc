#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    int H, W;
    cin >> H >> W;

    vector<int> height(W);
    for (int i = 0; i < W; i++) cin >> height[i];

    int total = 0;
    for (int i = 1; i < W - 1; i++) {
        int left = *max_element(height.begin(), height.begin() + i);
        int right = *max_element(height.begin() + i + 1, height.end());

        int water = min(left, right) - height[i];
        if (water > 0) total += water;
    }

    cout << total << '\n';
}