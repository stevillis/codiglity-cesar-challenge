# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if 0 <= K <= 500:
        return days_of_week[(days_of_week.index(S) + K) % len(days_of_week)]


print(solution("Wed", 2))
print(solution("Sat", 23))
