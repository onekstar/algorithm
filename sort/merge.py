#coding:utf-8
import copy

def merge(l, p, q, r):
    '归并'

    l1 = copy.copy(l[p:q])
    l2 = copy.copy(l[q:r])
    i = j = 0
    while (i < len(l1) and j < len(l2)):
        if l1[i] > l2[j]:
            l[p+i+j] = l1[i]
            i = i+1
        else:
            l[p+i+j] = l2[j]
            j = j + 1
    while(i < len(l1)):
        l[p+i+j] = l1[i]
        i = i + 1
    while(j < len(l2)):
        l[p+i+j] = l2[j]
        j = j + 1

def sort(l, p, r):
    '排序'
 
    if p >= r - 1:
        return
    q = (p + r) / 2
    sort(l, p, q) 
    sort(l, q, r)
    merge(l, p, q, r)
    

if __name__ == '__main__':

    l = [1, 2, 4, 3, 54, 2, 6, 7, 5, 8, 10, 12, 45]
    sort(l, 0, len(l))
    print l
