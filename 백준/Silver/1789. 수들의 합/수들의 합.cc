/*
#include <bits/stdc++.h>

using namespace std;

int main() {
    long long S;
    cin >> S;

    int sum = 0, count = 0;
    for (int i=1; i<S;i++) {
        if (sum + i == S) {
            count++;
            break;
        } else if (sum + i < S) {
            sum += i;
            count++;
        } else {
            break;
        }
    }

    cout << count;
}
*/


#include <iostream>
using namespace std;

int main() {
    long long S;
    cin >> S;

    long long sum = 0;
    int count = 0;

    for (int i = 1; ; i++) {
        if (sum + i > S) break;
        sum += i;
        count++;
    }

    cout << count << '\n';
    return 0;
}
