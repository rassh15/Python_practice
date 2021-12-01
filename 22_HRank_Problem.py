'''
Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions  and  in group A. The second word, 'c', does not appear in group A, so print .

Expected output:

1 3
-1

'''

n, m = 5, 3

alist = ['a','b','c','a','c']
blist = ['c','a','d']

for b in blist:
    print()
    for i in range(1,len(alist)+1):
        if alist[i-1] == b:
            print(i, end=' ')
        elif b not in alist:
            print(-1)
            break
        