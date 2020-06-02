import math

MAXDATA = 1000

def adjust_heap(H, i):
    parent = i
    temp = H[i]
    while len(H) - 1 >= 2 * parent:
        child = 2 * parent
        if len(H) - 1 > child and H[child + 1] > H[child]:
            child += 1
        if H[parent] >= H[child]:
            break
        else:
            H[parent] = H[child]
            parent = child
            H[parent] = temp
    return H

def create_heap(H):
    for j in range(math.floor((len(H)-1) / 2), 0, -1):
        H = adjust_heap(H, j)
    return H

heap = [MAXDATA, 9, 30, 38, 43, 49, 55, 66, 72, 79, 83, 87, 91]
heap = create_heap(heap)
for j in range(1, len(heap)):
    print('%-4d' % heap[j], end='')
