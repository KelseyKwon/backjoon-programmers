#include <bits/stdc++.h>

using namespace std;

bool Comparator(const int &a, const int &b) {
    return (a >= b);
}

int main() {
    string str;
    cin >> str;

    vector<int> nums(str.size(), 0);

    for (int i=0; i<str.size(); i++) {
        nums[i] = stoi(str.substr(i, 1));
    }

    sort(nums.begin(), nums.end(), Comparator);
    for (int i: nums) {
        cout << i;
    }
}