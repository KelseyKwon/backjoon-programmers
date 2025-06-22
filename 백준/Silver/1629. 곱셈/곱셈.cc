#include <bits/stdc++.h>
using namespace std;

long long fast_pow(long long A, long long B, long long C) {
    if (B == 0) return 1;

    long long half = fast_pow(A, B / 2, C);
    long long res = (half * half) % C;

    if (B % 2 == 0) {
        return res;
    } else {
        return (res * A) % C;
    }
}

int main() {
    long long A, B, C;
    cin >> A >> B >> C;

    cout << fast_pow(A, B, C) << '\n';
    return 0;
}
