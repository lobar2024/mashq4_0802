a = list(map(int, input().split()))
ok = True

for i in range(len(a)-1):
    if a[i] >= a[i+1]:
        ok = False
        break

print("ha" if ok else "yo'q")
