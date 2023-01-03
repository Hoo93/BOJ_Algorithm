import sys

index = int(sys.stdin.readline().rstrip())
name_set = set()
discard_list = []

name_set.add(666)
for i in range(10):
    name_set.add(i*1000 + 666)
    name_set.add(6660+i)
    name_set.add(66600+i)
    name_set.add(666000+i)
    name_set.add(6660000+i)

#666~9666 // 6660~6669

for i in range(10,100):
    name_set.add(i*1000 +666)
    name_set.add((i//10)*10000 +6660+(i%10))
    name_set.add(66600+i)
    name_set.add(666000+i)
# 10666~99666 , 16660~96669 , 66610~66699
    
for i in range(100,1000):
    name_set.add(i*1000 +666)
    name_set.add((i//10)*10000 +6660+(i%10))
    name_set.add((i//100)*100000 +66600+(i%100))
    name_set.add(666000+i)

for i in range(1000,4000):
    name_set.add(i*1000 +666)
    name_set.add((i//10)*10000 +6660+(i%10))
    name_set.add((i//100)*100000 +66600+(i%100))
    name_set.add((i//1000)*1000000 +666000+(i%1000))

name_list = sorted(name_set)

print(name_list[index-1])
