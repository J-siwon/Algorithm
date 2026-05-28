#include <iostream>
#include<string>
#include<stack>
#include <algorithm>
using namespace std;

int solution(string s)
{
    int answer = -1;
    stack<int> arr;
    for (int i = 0; i< s.size(); i++)
    {
        if (arr.size() > 0 && arr.top() == s[i])
        {
            arr.pop();
        }
        else
        {
            arr.push(s[i]);
        }
    }

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << arr.size();
    if (arr.size() == 0)
        answer = 1;
    else
        answer = 0;

    return answer;
}