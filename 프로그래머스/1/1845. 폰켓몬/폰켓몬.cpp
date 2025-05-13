#include <vector>
#include <unordered_set>
using namespace std;

int solution(vector<int> nums)
{
    unordered_set<int> count_kinds;
    int total_nums = nums.size() / 2;
    for (int number : nums) {
        count_kinds.insert(number);
    }

    if (count_kinds.size() < total_nums) {
        return count_kinds.size();
    } else {
        return total_nums;
    }
    
}