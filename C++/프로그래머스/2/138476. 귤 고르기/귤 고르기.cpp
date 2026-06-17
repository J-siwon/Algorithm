#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    unordered_map<int, int> um;
    
    for (int i : tangerine) {
        um[i]++;
    }
    
    vector<int> counts;
    for (auto const& pair : um) {
        counts.push_back(pair.second);
    }
    
    sort(counts.rbegin(), counts.rend());
    
    int total = 0;
    for (int count : counts) {
        total += count;
        answer++;
        
        if (total >= k) {
            break;
        }
    }
    
    return answer;
}