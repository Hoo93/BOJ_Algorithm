num = input()
in_l = [ [] for _ in range(int(num))]

for i in range(int(num)):
    in_l[i].append(input().split())
    in_l[i].append(input().split())

def test_case(a : list,b : list):
    l = [ i+1 for i in range(int(a[0])) ]
    fin = l[int(a[1])]
    count = 0
    flag = '0'

    while flag != fin:
        n = 0
        for i in range(1,len(l)):
            if int(b[0]) < int(b[i]):
                b.append(b.pop(0))
                l.append(l.pop(0))
                n += 1
                break
        if n ==0:    
            b.pop(0)
            flag = l.pop(0)
            count += 1
    
    return count




for i in range(int(num)):
    print(test_case(in_l[i][0],in_l[i][1]))


        
      

