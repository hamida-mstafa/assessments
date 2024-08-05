def solution(A):
    if len(A) <= 1:
        return len(A)

    max_len = 2
    recent_len = 2

    for i in range(2, len(A)):
        recent_len = recent_len + 1 if A[i] == A[i - 2] else 2
        max_len = max(max_len, recent_len)

    return max_len

# Test cases
print(solution([3, 2, 3, 2, 3]))  # Output: 5
print(solution([7, 4, -2, 4, -2, -9]))  # Output: 4
print(solution([7, -5, -5, -5, 7, -1, 7]))  # Output: 3
print(solution([4]))  # Output: 1
