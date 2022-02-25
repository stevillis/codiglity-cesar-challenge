# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(D, S):
    if 1 <= D <= 5:
        multiply_dict = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5
        }
        return D * multiply_dict[S]


print(solution(4, "two"))
