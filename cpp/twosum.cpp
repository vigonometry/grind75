#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        map<int, int> m;
        for (int i = 0; i < nums.size(); ++i)
        {
            int n = target - nums[i];
            if (m.count(n))
            {
                return {m[n], i};
            }
            m[nums[i]] = i;
        }
        return {};
    }
};

int main()
{
    Solution s;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = s.twoSum(nums, target);
    for (int i = 0; i < result.size(); ++i)
    {
        cout << result[i] << endl;
    }
    return 0;
}