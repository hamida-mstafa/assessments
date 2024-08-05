def solution(S):
    S = list(S)

    while any(int(S[i]) + int(S[i + 1]) <= 9 for i in range(len(S) - 1)):
        i = 0
        while i < len(S) - 1:
            if int(S[i]) + int(S[i + 1]) <= 9:
                S[i] = str(int(S[i]) + int(S[i + 1]))
                S.pop(i + 1)
            else:
                i += 1

    return ''.join(S)

# Test cases
print(solution("32581"))  # Output: "559"
print(solution("1119812"))  # Output: "3992"
print(solution("226228"))  # Output: "4828"