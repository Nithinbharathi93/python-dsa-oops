# m, n = map(int, input().split())
# block_count = int(input())
# bloacked_positions = []
# for i in range(block_count):
#     x, y = map(int, input().split())
#     if x<=0 or y<=0:
#         print("Enter valid cell position")
#     bloacked_positions.append((x, y))

m = n = 5
bloacked_positions = [(1, 1), (2, 0), (2 ,3)]

mat = [[1]*m for _ in range(n)]

ps = lambda x, pos: x[pos]

for i in range(m):
    for j in range(n):
        if (i, j) in bloacked_positions:
            mat[i][j] = "Nah"
        elif mat[i-1][j] in ["Nah", 0] and mat[i][j]!="Nah":
            mat[i][j] = 0

mat[0][0] = 0


for i in range(1, m):
    for j in range(1, n):
        sub = [x!="Nah" for x in [mat[i][j-1], mat[i-1][j], mat[i][j]]]
        if any(sub):
            if all(sub):
                mat[i][j] = mat[i][j-1] + mat[i-1][j]
            elif mat[i][j]!="Nah":
                if sum(sub)==1:
                    mat[i][j] = 0
                else:
                    mat[i][j] = mat[i][j-1] if mat[i][j-1]!="Nah" else mat[i-1][j]

print(f"+{f"{"":-<5}+"*n}")
for i in range(m):
    for j in range(n):
        print(f"|{mat[i][j]:^5}", end="")
    print("|")
    print(f"+{f"{"":-<5}+"*n}")
