/*
지금 이 코드의 치명적인 오류 : 그냥 단순히 사용 횟수로 비교하면,
10번 사용한 것이 나아아중에 사용되고 2번 사용될것이 먼저 사용되어도
10번 사용되는 것이 먼저 지워지기 때문에 치명적인 오류가 난다.

따라서 가장 나중에 사용될 plug을 지우는 것이 핵심!

#include <vector>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <algorithm>

using namespace std;

int N, K;
vector<int> product;
vector<int> plug;
vector<int> product_count;

int main() {
  int answer = 0;
  cin >> N >> K;

  product_count.resize(K+1, 0);

  for (int i=0; i<K; i++) {
    int product_name;
    cin >> product_name;
    product.push_back(product_name);
    product_count[product_name]++;
  }

  for (int i=0; i<K; i++) {
    if (!(find(plug.begin(), plug.end(), product[i]) != plug.end())) {
      product_count[product[i]] -= 1;
      continue;
    }

    if (plug.size() < N) {
      plug.push_back(product[i]);
      product_count[product[i]]-=1;
    } else {
      // todo : 가장 count가 작은 것을 삭제하기
      int cur_count = product_count[plug[0]];
      int will_be_deleted = plug[0];
      for (int j=1; j<plug.size(); j++) {
        if (product_count[plug[j]] < cur_count) {
          will_be_deleted = plug[j];
          cur_count = product_count[plug[j]];
        }
      }
      plug.erase(remove(plug.begin(), plug.end(), will_be_deleted), plug.end());
      plug.push_back(product[i]);
      answer += 1;
    }
  }
  cout << answer;
}
  */

  #include <iostream>
  #include <vector>
  #include <algorithm>
  
  using namespace std;
  
  int main() {
      int N, K;
      cin >> N >> K;
      vector<int> order(K);
      for (int i = 0; i < K; i++) cin >> order[i];
  
      vector<int> plug;
      int answer = 0;
  
      for (int i = 0; i < K; i++) {
          // 이미 꽂혀 있으면 continue
          if (find(plug.begin(), plug.end(), order[i]) != plug.end()) continue;
  
          // 빈 자리 있음
          if (plug.size() < N) {
              plug.push_back(order[i]);
              continue;
          }
  
          // 가장 나중에 다시 사용되거나, 다시 사용되지 않는 것 제거
          int idx_to_remove = -1, latest_use = -1;
  
          for (int j = 0; j < N; j++) {
              int next_use = K + 1;
              for (int k = i + 1; k < K; k++) {
                  if (order[k] == plug[j]) {
                      next_use = k;
                      break;
                  }
              }
              if (next_use > latest_use) {
                  latest_use = next_use;
                  idx_to_remove = j;
              }
          }
  
          plug[idx_to_remove] = order[i];
          answer++;
      }
  
      cout << answer;
  }
  