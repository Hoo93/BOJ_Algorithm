import sys

n,m= list(map(int,sys.stdin.readline().rstrip().rsplit()))

pokemon_dict = {}
pokemon_list = []
test_list = []
for i in range(n):
    pokemon = sys.stdin.readline().rstrip()
    pokemon_dict.update({pokemon:i+1})
    pokemon_list.append(pokemon)

for i in range(m):
    test_list.append(sys.stdin.readline().rstrip())

for word in test_list:
    if ord(word[0]) >= 65:
        print(pokemon_dict[word])
    else:
        print(pokemon_list[int(word)-1])