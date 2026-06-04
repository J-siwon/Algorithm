using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        // brown + yellow = x * y
        // yellow = (x-1) * (y-1)
        for (int x = 1; x <= brown; x++)
        {
            if ((brown + yellow) % x != 0)
                continue;
            int y = (brown + yellow) / x;
            Console.WriteLine($"{x}, {y}");
            if ((x-2) * (y-2) == yellow)
            {
                Console.WriteLine("Approved");
                answer[0] = y;
                answer[1] = x;
                break;
            }
                
        }
        
        return answer;
    }
}