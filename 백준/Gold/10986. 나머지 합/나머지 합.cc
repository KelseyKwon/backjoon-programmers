#include <bits/stdc++.h>

using namespace std;

int N, M;
long long remainders[1001];

int main() {
    cin >> N >> M;
    remainders[0]++;
    long long sum = 0;

    for (int i=1; i<=N; i++) {
        int num;
        cin >> num;
        sum += num;
        remainders[sum % M]++;
    }

    long long sums = 0;
    for (int i=0; i<M; i++) {
        if (remainders[i] > 0) {
            sums += (remainders[i] * (remainders[i] - 1)) / 2;
        }
    }

    cout << sums;
}