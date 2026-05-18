#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    
    stack<int> q;
    for (char i : s)
    {
        if (i == '(')
        {
            q.push(i);
        }
        else
        {
            if (q.size() == 0)
            {
                answer = false;
                break;
            }
            
            q.pop();
        }
    }
    if (q.size() > 0)
        answer = false;

    return answer;
}