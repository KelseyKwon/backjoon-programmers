#include <bits/stdc++.h>
using namespace std;

int N, M;

vector<int> nums;
vector<int> result; 

void backtrack(int k, int start) {
    if (k == M) {
        for (int i : result) {
            cout << i << " ";
        }
        cout << '\n';
        return;
    }

    // 1 7 9 9
    // 1 
    int prev = 0;
    for (int i=start; i<nums.size(); i++) {
        if (prev != nums[i]) {
            prev = nums[i];
            result.push_back(nums[i]);
            backtrack(k+1, i);
            result.pop_back();
    }
}
}

int main()
{
    cin >> N >> M;
    nums.resize(N);
    for (int i = 0; i < N; i++)
    {
        cin >> nums[i];
    }
    sort(nums.begin(), nums.end());
    backtrack(0, 0);
    // 1 7 9 9
    return 0;
}