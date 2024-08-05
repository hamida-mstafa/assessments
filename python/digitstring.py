def solution(S):
    digits = list(map(int, S))
    i = 0
    
    while i < len(digits) - 1:
        if digits[i] + digits[i + 1] <= 9:
            digits[i] = digits[i] + digits[i + 1]
            del digits[i + 1]
            if i > 0:
                i -= 1
        else:
            i += 1
    
    return ''.join(map(str, digits))
print(solution("226228"))  
