#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin>>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
// 1-2+3-4+5-6+7...
        int N;
        cin >> N;
        
        int result = 0;
        if (N % 2 == 0) {
            result = -1 * (N/2);
        } else {
            result = -1 * ((N-1) / 2) + N;
        }
        
        cout << "#" << test_case << " " << result << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}