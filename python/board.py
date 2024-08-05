def solution(A):
    N = len(A)
    
    if N == 1:
        return 1

    A.sort()

    def is_possible(board_length):
        last_position = A[0]
        boards_count = 1

        for position in A:
            if position - last_position > board_length:
                last_position = position
                boards_count += 1

        return boards_count

    lower_bound, upper_bound = 1, A[-1] - A[0]

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if is_possible(mid) <= 2:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1

    return lower_bound

# Test cases
print(solution([11, 21, 14]))  # Output: 3
print(solution([15, 20, 9, 11]))  # Output: 5
print(solution([0, 44, 32, 30, 42, 18, 34, 16, 35]))  # Output: 18
print(solution([9]))  # Output: 1
