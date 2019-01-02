
# coding: utf-8

# # 1. Find angle MBC

# In[ ]:


import math
ab = float(input())
bc = float(input())
ac = math.sqrt((ab**2)+(bc**2))
bm = ac / 2.0
mc = bm
#let, 
a = bm
b = bc
c = mc
#where a=c
angle_c_radian = math.acos(b / (2*c))
angle_c_degree = int(round((180 * angel_c_radian) / math.pi))
output = str(angel_c_degree)+'°'
print(output)


#  # 2. Validating Credi card numbers

# In[ ]:


import re
i = int(input())
for c in range(i):
    credit = input().strip()
    credit_removed_hiphen = credit.replace('-','')
    valid = True
    length_16 = bool(re.match(r'^[4-6]\d{15}$',credit))
    length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',credit))    
    consecutive = bool(re.findall(r'(?=(\d)\1\1\1)',credit_removed_hiphen))
    if length_16 == True or length_19 == True:
        if consecutive == True:
            valid=False
    else:
        valid = False       
    if valid == True:
        print('Valid')
    else:
        print('Invalid')


# # 3. Regex Substitution

# In[ ]:


import re, sys
n = int(input())
for line in sys.stdin:
    remove_and = re.sub(r'(?<= )(&&)(?= )',"and",line)
    remove_or = re.sub(r'(?<= )(\|\|)(?= )',"or",remove_and)
    print(remove_or,end='')


# # 4. Reduce Function

# In[ ]:


from fractions import Fraction
from functools import reduce
def product(data):
    t = Fraction(reduce(lambda x,y : x*y,data))
    return t.numerator, t.denominator
if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
        data.append(Fraction(*map(int, input().split())))
    result = product(data)
    print(*result)


# # 5. ginortS

# In[ ]:


s = input()
s = sorted(s,key = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),x))
print(*(s),sep = '')


# # 6. Triangle Quest

# In[ ]:


for i in range(1,int(input())):
    print((10**i)//9*i)


# # 7. Piling Up

# In[ ]:


from collections import deque
data = int(input())
for t in range(data):
    n = int(input())
    dq = deque(map(int,input().split()))
    possible = True
    element = (2**31)+1
    while dq:
        left_element = dq[0]
        right_element = dq[-1]
        if left_element>=right_element and element>=left_element:
            element = dq.popleft()
        elif right_element>=left_element and element>=right_element:
            element = dq.pop()
        else:
            possible = False
            break
    if possible:
        print('Yes')
    else:
        print('No')  


# # 8. Compress the string

# In[ ]:


import itertools
data = input().strip()
data_unique_element = list(set(data))
group = []
key = []
for i,c in itertools.groupby(data):
    group.append(list(c))
    key.append(i)
for i in range(len(group)):
    group_length = len(group[i])
    i = int(key[i])
    print(tuple((group_length,i)),end=' ')


# # 9. Iterables and Iterators

# In[ ]:


from itertools import combinations
n = int(input())
ar = input().split()
k = int(input())
comb_list = list(combinations(ar,k))
a_list = [e for e in comb_list if 'a' in e]
print(len(a_list) / len(comb_list))


# # 10. The Minion Game

# In[ ]:


s = input().strip()
s_length = len(s)
vowel_list = ['A','E','I','O','U']
stuart_point = 0
kevin_point = 0
for i in range(s_length):
    if s[i] in vowel_list:
        kevin_point += s_length - i
    else:
        stuart_point += s_length - i
if stuart_point == kevin_point:
    print('Draw')
elif kevin_point > stuart_point:
    print('Kevin',kevin_point)
else:
    print('Stuart',stuart_point)

