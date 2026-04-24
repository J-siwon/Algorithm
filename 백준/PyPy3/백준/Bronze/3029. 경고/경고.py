import sys
import math
from collections import deque, Counter
from datetime import datetime
# sys.setrecursionlimit(5*10**5)

t1 = input().strip()
t2 = input().strip()

diff = datetime.strptime(t2, '%H:%M:%S') - datetime.strptime(t1, '%H:%M:%S')
seconds = int(diff.total_seconds())
if seconds <= 0:
    seconds += 24 * 60 * 60

# 시, 분, 초 계산
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

# f-string을 이용한 포맷팅 (결과: 00:10:00)
print(f"{hours:02}:{minutes:02}:{seconds:02}")