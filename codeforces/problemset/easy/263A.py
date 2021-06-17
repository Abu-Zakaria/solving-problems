# https://codeforces.com/problemset/problem/263/A
moves = 0
for i in range(5):
    items = input().split(" ")
    for j in range(len(items)):
        if items[j] == "1":
            moves += abs(3 - (j + 1)) + abs(3 - (i + 1))
            break
print(moves)
