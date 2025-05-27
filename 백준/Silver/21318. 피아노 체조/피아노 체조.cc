/*
1 <= N인 x, y을 골라서 x번부터 y번까지 번호 순서대로 연주하기

현재 악보가 바로 다음악보보다 어려우면 실수. (즉, 현재 숫자가 다음 숫자보다 높으면 실수)
마지막은 다음보다 높은지 낮은지 알 수 없으므로 실수 x.

1 2 3 3 4 1 10 8 1

1 2 3 
2 3 3 4
3 4 1 10 -> 4에서 실수
8 (같으니까 실수 x)
4 1 10 8 1 -> 4, 10, 8에서 실수

일단 배열에 담아. 
*/

/*
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, Q;

int main() {
  cin >> N;
  vector<int> rates(N+1, 0);

  for (int i=1; i<=N; i++) {
    cin >> rates[i];
  }

  cin >> Q;

  vector<vector<int>> btw;
  for(int i=0; i<Q; i++) {
    int u, w;
    cin >> u >> w;
    vector<int> sliced(rates.begin() + u, rates.begin() + u + w); //벡터 슬라이스 하는법
    btw.push_back(sliced);
  }


  vector<int> answers;
  for (int i=0; i<Q; i++) {
    int count = 0;
    if (btw[i].size() == 1) {
      answers.push_back(0);
      continue;
    }
    for (int j=0; j<btw[i].size()-2; i++) {
      if (btw[i][j] > btw[i][j+1]) {
        count += 1;
      }
    }
    count += 1;
    answers.push_back(count);
  }

  for (int i : answers) {
    cout << i << endl;
  }
}
*/

/*
시간 초과
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, Q;

int main() {
  cin >> N;
  vector<int> rates(N+1, 0);

  for (int i=1; i<=N; i++) {
    cin >> rates[i];
  }

  cin >> Q;

  vector<int> answers;
  for(int i=0; i<Q; i++) {
    int u, w;
    int count = 0;
    cin >> u >> w;
    for (int j=u; j<w; j++) {
      if (rates[j] >= rates[j+1]) {
        count+=1;
      }
    }
    answers.push_back(count);
  }

  for (int i : answers) {
    cout << i << endl;
  }
}

누적합 방식 : 0 0 0 0 1 0 1 1 0
          0 0 0 0 1 1 2 3 3

  */

  #include <iostream>
  #include <vector>
  
  using namespace std;
  
  int N, Q;
  
  int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    vector<int> rates(N+1, 0);
    vector<int> rating(N, 0);
    vector<int> prefix_sum(N, 0);
  
    for (int i=1; i<=N; i++) {
      cin >> rates[i];
    }
    
    for (int i=1; i<N; i++) {
      if (rates[i] > rates[i+1]) {
        rating[i] = 1;
      }
    }

    for (int i=1; i<N; i++) {
      prefix_sum[i] = prefix_sum[i-1] + rating[i];
    }

    int Q;
    cin >> Q;
    while (Q--) {
      int u, v;
      cin >> u >> v;
      if (u == v) {
        cout << 0 << '\n';
      } else {
        cout << prefix_sum[v-1] - prefix_sum[u-1] << '\n';
      }
    }
  }