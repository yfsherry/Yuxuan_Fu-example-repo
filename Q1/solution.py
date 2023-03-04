import sys
n1 = int(input())
total = input().split(' ')
n2 = int(input())
order = input().split(' ')

def rank(size):
    if 'M' in size:
        rk = 0
    elif 'S' in size:
        rk = - len(size)
    else:
        rk = len(size)
    return rk

trk = list(map(rank, total))
ork = list(map(rank, order))

for i in range(len(order)):
    if trk[-1] >= ork[-1]:
        trk.pop()
        ork.pop()
    else:
        # print('No')
        break
if len(ork) != 0:
    print('No')
else:
    print('Yes')
        

    
