
# coding: utf-8

# In[1]:

def match_ends(words):
    count=0
    for word in words:
        if len(word)>=2 and word[0]== word[len(word)-1] : count+=1
    return count

#print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])


# In[2]:

def front_x(words):
    list_x=[]
    list_other=[]
    list_final=[]
    for word in words:
        if word[0].lower()=="x" : list_x.append(word)
        else : list_other.append(word)
    return sorted(list_x)+sorted(list_other)

#print front_x(["Xest","ok","apzihra","xao"])


# In[3]:

def sort_last(tuples):
    return sorted(tuples,key=lambda last: last[len(last)-1]) 

#print sort_last( [(1, 7), (1, 3), (3, 4, 5), (2, 2)] )


# In[4]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# In[5]:

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


# In[6]:

main()


# In[72]:

def remove_adjacent(nums):
    i=0
    while i < len(nums)-1:
        """
        print "lvl : ", i
        print nums
        print "i =",i ," et i+1 = ",i+1
        print nums[i]," ==  ",nums[i+1]
        """
        if nums[i]==nums[i+1] : 
            #print "retire : ", i+1,", Valeur :",nums[i+1]
            del nums[i+1]
            #print nums
        else :
            i+=1
    return nums

#print remove_adjacent([2, 2, 2,3, 3, 3,5,5,5,5,5])


# In[77]:

def linear_merge(list1, list2):
    list_merge=[]
    list_merge=list1+list2
    return sorted(list_merge)

#linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])


# In[74]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# In[78]:

def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])


# In[79]:

main()


# 
