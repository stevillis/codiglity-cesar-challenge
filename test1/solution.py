

# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")

def solution(N):
    character = 'L'
    ascii_art = []
    if 1 <= N <= 100:
        for _ in range(N - 1):
            print(character)
        for _ in range(N):
            ascii_art.append(character)
        print(''.join(ascii_art))


with open('./test1/test-input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        solution(int(line))
