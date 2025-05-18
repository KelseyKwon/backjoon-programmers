#include<iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
	for (int i=0; i<10; i++) {
     int N;
        cin >> N;
        vector<int> buil_height(N);
        
        for (int i=0; i<N; i++) {
         cin >> buil_height[i];
        }
        
        int answer = 0;
        for (int i=2; i<N-2; i++) {
            vector<int> neighbors(4);
            neighbors.push_back(buil_height[i-2]);
            neighbors.push_back(buil_height[i-1]);
            neighbors.push_back(buil_height[i+1]);
            neighbors.push_back(buil_height[i+2]);
            int max_neighbor = *max_element(neighbors.begin(), neighbors.end());
            
            if (max_neighbor < buil_height[i]) {
             answer += buil_height[i] - max_neighbor;   
            }
        }
        
        cout << "#" << i+1 << " " << answer << endl;
    }
	return 0;
}