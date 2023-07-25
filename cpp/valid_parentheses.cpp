#include <iostream>
#include <stack>
#include <map>

using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        map<char, char> m{{')','('}, {'}','{'}, {']','['}};
        for (char c: s) {
            if ((c == '(') || (c == '{') || (c == '[')) {
                stk.push(c);
            } else {
                if (stk.empty() || stk.top() != m[c]) {
                    return false;
                }
                stk.pop();
            }
        }
        return stk.empty();
    }
};

int main(){
    Solution s;
    string str = "()[]{}";
    cout << s.isValid(str) << endl;
    return 0;
}