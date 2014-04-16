#coding:utf-8

def sort(l, left, right):
    '快速排序'

    if left >= right:
        return
    i = left
    k = right
    key = l[left]
    while left < right:
        while True and (left < right):
            if l[right] <= key:
                l[left] = l[right] 
                break
            else:
                right -= 1
        while True and (left < right):
            if l[left] > key:
               l[right] = l[left] 
               break
            else:
                left += 1
    l[left] = key
    sort(l, i, left - 1) 
    sort(l, left + 1, k)
            

if __name__ == '__main__':
    
    l = [1, 4, 3, 2, 0, 5, -1, -3, 59, 8 ,7, 2]
    sort(l, 0, len(l) - 1)
    print l
    
