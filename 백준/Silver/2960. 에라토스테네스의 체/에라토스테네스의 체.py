N,K = map(int,input().rstrip().split())


if N//2 >= K:
    print(2*K)

else:
    K -= N//2
    idx = 3
    flag = True

    seives = [ True for _ in range(N+1)]
    for i in range(2,N+1,2):
        seives[i] = False
    
    for idx in range(3,N+1,2):
        if not flag:
            break

        if not seives[idx]:
            continue

        for i in range(idx,N+1,idx):
            if seives[i]:
                K -= 1
                seives[i] = False
                if K == 0:
                    flag = False
                    print(i)
            else:
                continue
