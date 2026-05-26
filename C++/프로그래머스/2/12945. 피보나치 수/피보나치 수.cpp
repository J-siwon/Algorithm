#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> arr;
    arr.push_back(0);
    arr.push_back(1);
    for(int i = 2; i<=n; i++)
    {
        arr.push_back((arr[arr.size()-1] + arr[arr.size()-2]) % 1234567);
    }
    answer = arr.back();
    
    return answer;
}