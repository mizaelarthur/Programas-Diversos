def hanoi (n,d,p,u):
    if n==1:
        print("Mova o disco 1 de ",d," para ",p)
    else:
        hanoi(n-1,d,u,p)
        print("Mova o disco ",n,' de ',d,' para ',d)
        hanoi (n-1,u,p,d) 
hanoi(3,1,3,2)