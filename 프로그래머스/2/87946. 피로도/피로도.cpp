/*
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
// dungeons[i][0]이 필수피로도보다 낮으면, 끝.
// 아니면 계속 하기.
using namespace std;

vector<int> visited;

// 여기서의 문제점 : count = 1로 계속 초기화해주고 있기 때문에 계속 1만 나온다.
int backtrack(int start, vector<int> visited, vector<vector<int>> dungeons) {
  int count = 1;
  for (int i=0; i<visited.size(); i++) {
    if (dungeons[i][0] < start) {
      break;
    }
    if (!visited[i] && dungeons[i][0] >= start) {
      visited[i] = true;
      count+=1;
      backtrack(start - dungeons[i][0], visited, dungeons);
      count-=1;
    }
  }
  return count;
}

int solution(int k, vector<vector<int>> dungeons) {
  int answer = -1;
  visited.resize(dungeons.size(), 0);

  for (int i=0; i<dungeons.size(); i++) {
    if (dungeons[i][0] >= k) {
      visited[i] = 1;
      int temp = backtrack(i, visited, dungeons);
      answer = max(temp, answer);
    }
  }

  return answer;
}
  */

#include <algorithm>
#include <vector>

using namespace std;

vector<int> visited;
int answer = 0;

// 여기서의 문제점 : count = 1로 계속 초기화해주고 있기 때문에 계속 1만 나온다.
void backtrack(int fatigue, int depth, vector<vector<int>>& dungeons) {
  answer = max(depth, answer);
  for (int i=0; i<dungeons.size(); i++) {
    int min_fatigue = dungeons[i][0]; 
    int sold_fatigue = dungeons[i][1];
    if (!visited[i] && fatigue >= min_fatigue) {
      visited[i] = true;
      backtrack(fatigue - sold_fatigue, depth+1, dungeons);
      visited[i] = false;
    }
  }
}

int solution(int k, vector<vector<int>> dungeons) {
  visited.resize(dungeons.size(), 0);
  backtrack(k, 0, dungeons);
  return answer;
}