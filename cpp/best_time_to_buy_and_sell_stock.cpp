#include <vector>

using namespace std;

class Solution {
public:
    //Kadane's algorithm
    int max (int a, int b) {
        return a > b ? a : b;
    }
    
    int maxProfit(vector<int>& prices) {
        int lsum = 0, gsum = 0;
        for (int i = 1; i < prices.size(); ++i) {
            lsum = max(0, lsum + prices[i] - prices[i - 1]);
            gsum = max(lsum, gsum);
        }
        return gsum;
    }
};