#include <vector>
#include <iostream>
#include <climits>

using namespace std;
int N, S;
vector<int> nums;

int main() {
    cin >> N >> S;
    nums.resize(N+1, 0);

    for (int i=1; i<=N; i++) {
        cin >> nums[i];
    }

    int start = 1, end = 1;
    int sum = nums[1];
    int answer = INT_MAX;
    while (start <= end && end <= N) {
        if (sum >= S) answer = min(answer, end-start+1);
        if (sum < S) {
            end++;
            sum += nums[end];
        } else {
            sum -= nums[start];
            start++;
        }
    }

    if (answer == INT_MAX) cout << 0 << '\n';
    else cout << answer << '\n';
    return 0;
}