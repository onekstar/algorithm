#coding:utf-8
import copy

def merge(l, p, q, r):
    '归并'

    l1 = copy.copy(l[p:q])
    l2 = copy.copy(l[q:r])
    i = j = 0
    count = 0
    while (i < len(l1) and j < len(l2)):
        if l1[i] <= l2[j]:
            l[p+i+j] = l1[i]
            i = i + 1
        else:
            l[p+i+j] = l2[j]
            j = j + 1
            count += 1
    count += (len(l1) - i - 1) * len(l2)
    while(i < len(l1)):
        l[p+i+j] = l1[i]
        i = i + 1
    while(j < len(l2)):
        l[p+i+j] = l2[j]
        j = j + 1
    return count

def find_inversion(l, p, r):
    '排序'
 
    if p >= r - 1:
        return 0
    q = (p + r) / 2
    a = find_inversion(l, p, q) 
    b = find_inversion(l, q, r)
    c = merge(l, p, q, r)
    return a + b + c
    

if __name__ == '__main__':
    
    l = [3, 2, 1, 0]
    print find_inversion(l, 0, len(l))
    print l
