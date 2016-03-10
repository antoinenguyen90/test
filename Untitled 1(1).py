
# coding: utf-8

# In[104]:

def donuts(count):
    string=""
    if count<10 : string+="Number of donuts: %d" %count
    else : string+= "Number of donuts: many"
    return string


# In[111]:

def both_ends(s):
    string=""
    if len(s)>=2: string+=s[0]+s[1]+s[len(s)-2]+s[len(s)-1]
    return string


# In[112]:

def fix_start(s):
    string=""
    string+=s[0]+s[1:].replace(s[0],"*")
    return string
#print fix_start("babble")


# In[113]:

def mix_up(a, b):
    string=""
    string+=b[0:2]+a[2:len(a)]+" "+a[0:2]+b[2:len(b)]
    return string

#print mix_up('mix', 'pod') 


# In[114]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# In[115]:

def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# In[116]:

main()


# In[118]:

def verbing(s):
    string=""
    string+=s
    if len(s)>=3:
        if s[len(s)-3:len(s)]=="ing": string +="ly"
        else : string +="ing" 
    return string

print verbing('hail')
print verbing('swiming')
print verbing('do')


# In[144]:

def not_bad(s):
    if s.find("not")<s.find("bad"):
        return s[0:s.find("not")]+"good"+s[s.find("bad")+3:len(s)]
    return s 


# In[145]:

def front_back(a, b):
    a_front=""
    a_back=""
    b_front=""
    b_back=""
    if len(a)%2==0 :
        a_front+=a[0:len(a)/2]
        a_back+=a[len(a)/2:len(a)]
    else :
        a_front+=a[0:len(a)/2+1]
        a_back+=a[len(a)/2+1:len(a)]
    if len(b)%2==0 :
        b_front+=b[0:len(b)/2]
        b_back+=b[len(b)/2:len(a)]      
    else:
        b_front+=b[0:len(b)/2+1]
        b_back+=b[len(b)/2+1:len(a)] 
    return a_front+b_front+a_back+b_back


# In[146]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# In[147]:

def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# In[148]:

main()


# In[ ]:



