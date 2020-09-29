# --------------
def palindrome(num):
    while True:
        num+=1
        if str(num) == str(num)[::-1]:
            return num

palindrome(123)


# --------------
def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)





# --------------
#Code starts here
import math
def check_fib(num):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * num
    return num == 0 or abs(round(a) - a) < 1.0 / num


# --------------
#Code starts here
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)


# --------------
#Code starts here
def k_distinct(string,k):
    s_list=(set(string.lower()))
    return len(s_list)>=k


