# https://codeforces.com/problemset/problem/231/A
n = int(input())
can_do = 0
for i in range(n):
    _can_do = 0
    for x in input().split(" "):
        if x == "1":
            _can_do += 1
    if _can_do > 1:
        can_do += 1
print(can_do)
