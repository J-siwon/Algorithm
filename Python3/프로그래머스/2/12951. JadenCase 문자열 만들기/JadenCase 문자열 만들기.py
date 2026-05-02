def solution(s):
    answer = ''
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    isfinding = True
    for i in s:
        if i == " ":
            isfinding = True
            answer += i
            continue
        
        if not isfinding:
            answer += i.lower()
        else:
            answer += i.upper()
            isfinding = False
        
    return answer