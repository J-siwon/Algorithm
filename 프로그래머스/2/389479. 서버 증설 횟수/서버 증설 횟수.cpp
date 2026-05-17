#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> players, int m, int k) {
    //m명 미만이면 서버 증설 필요 x 
    //n개의 서버가 운영중이면 nm ~ (n+1)m
    //한번 증설한 서버는 k시간만 운영
    
    //닫히는 시간을 담을 5칸짜리 배열
    queue<int> stop_times;
    int now = 0;
    int answer = 0;
    for (int i = 0; i < players.size(); i++)
    {
        while(!stop_times.empty() && stop_times.front() == i) 
        {
            cout << stop_times.back() << " poped";
            stop_times.pop();
        }
        
        while ((stop_times.size()+1) * m <= players[i])
        {
            stop_times.push(i+k);
            answer += 1;
            cout << i;
        }
        cout << endl;
    }
    
    
    return answer;
}