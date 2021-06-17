#https://codeforces.com/problemset/problem/282/A
n = int(input())
val = 0
for i in range(n):
    statement = input()
    if len(statement) != 3:
        continue
    if (statement[0:2] == "++" and statement[2:3].lower() == "x" or
        statement[0:1].lower() == "x" and statement[1:3] == "++"):
        val += 1
    elif (statement[0:2] == "--" and statement[2:3].lower() == "x" or
        statement[0:1].lower() == "x" and statement[1:3] == "--"):
        val -= 1
print(val)
