#coding:utf-8

def sort(l):
    '对l进行排序'

    print 'INPUT : %s' %l
    for i in range(1, len(l)):
        t = l[i] 
        for j in range(i -1, -1, -1):
            if l[j] > t:
                l[j + 1] = l[j]
                l[j] = t
            else:
                break
    print 'OUTPUT: %s' %l

if __name__ == '__main__':
    
    import random
    l = []
    for i in xrange(2):
       l.append(random.randint(1, 1000)) 
    sort(l)
