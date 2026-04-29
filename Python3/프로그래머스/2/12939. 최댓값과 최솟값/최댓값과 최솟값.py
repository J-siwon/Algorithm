def solution(s):
    answer = [int(i) for i in s.split(' ')]
    return f'{min(answer)} {max(answer)}'