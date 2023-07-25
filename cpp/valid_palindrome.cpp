#include <iostream>
#include <cctype>

using namespace::std;

class Solution {
public:
    bool isPalindrome(string s) {
        int st = 0, e = s.size() - 1;
        while (st < e) {
            if (!isalnum(s[st])) {
                st++;
                continue;
            }
            
            if (!isalnum(s[e])) {
                e--;
                continue;
            }
            
            if (tolower(s[st++]) != tolower(s[e--])) {
                return false;
            }
        }
        return true;
    }
};