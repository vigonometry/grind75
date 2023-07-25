#include <iostream>
#include <map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> m;
        for (char c : s) {
            m[c]++;
        }
        
        for (char c : t) {
            m[c]--;
        }
        
        for (auto x : m) {
            if (x.second) {
                return false;
            }
        } 
        return true;
    }
};