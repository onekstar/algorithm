#coding:utf-8

def reverse(s):
    '反转字符串'

    if len(s) <= 1:
        return s
    m = len(s) / 2
    s1 = s[0:m]
    s2 = s[m:len(s)]
    s1 = reverse(s1)
    s2 = reverse(s2)
    return '%s%s' %(s2, s1)

if __name__ == '__main__':
    
    s = 'abcdefg'
    print reverse(s)
