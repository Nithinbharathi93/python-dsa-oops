player_power = int(input("Enter player power: "))
monster_count = int(input("Enter monster count: "))
l = []
for i in range(monster_count):
    l.append(tuple(map(int, input().split())))
w
l = sorted(l, key=lambda x:x[0])
count = 0
for i, j in l:
    if i<=player_power:
        player_power += j 
        count += 1
print(f"Slaughterde {count} monsters")
 