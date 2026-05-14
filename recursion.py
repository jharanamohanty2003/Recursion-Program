#sum of digits of a number
'''def Add_digits(num):
    if num==0:
        return 0
    return (num%10)+Add_digits(num//10)
num=125
print(Add_digits(num))'''

#armstrong
'''def ArmStrong(num,power):
    if num==0:
        return 0
    return (num%10)**power+ArmStrong(num//10,power)
num=153
power=len(str(num))
if ArmStrong(num,power)==num:
    print('Armstrong number')
else:
    print('not armstrong number')'''

'''def ArmStrong(num,power):
    rem=num%10
    if num==0:
        return 0
    return rem**power+ArmStrong(num//10,power)
num=153
power=len(str(num))
if ArmStrong(num,power)==num:
    print('armstrong')
else:
    print('not')'''

#disarum
'''def Disarum(num,power):
    if num==0:
        return 0
    return (num%10)**power+Disarum(num//10,power-1)
num=135
power=(len(str(num)))
if Disarum(num,power)==num:
       print('disarum')
else:
    print('not')'''

#factorial
'''def Factorial(num):
    if num<0:
        return 'not possible'
    if num==0 or num==1:
        return 1
    return num*Factorial(num-1)
num=5
print(Factorial(num))'''

#integer to binary
'''def Binary(num,place):
    if num==0:
        return 0
    return (num%2)*place+Binary(num//2,place*10)
num=12
place=1
print(Binary(num,place))'''

'''def Binary(num,place):
    if num==0:
        return 0
    return (num%2)*place+Binary(num//2,place*10)
num=12
place=1
print(Binary(num,place))'''

#binary to integer
'''def Integer(num,power=0):
    if num==0:
        return 0
    return (num%10)*(2**power)+Integer(num//10,power+1)
    power+=1
num=1100
power=0
print(Integer(num,power))'''

#prime number
'''def Prime(num,val=1):
    if val>num:
        return 0
    if num%val==0:
        return 1+Prime(num,val+1)
    else:
        return 0+Prime(num,val+1)
num=3
if Prime(num)==2:
    print('prime')
else:
    print('not prime')'''

#palyprime
'''def Prime(num,val=1):
     if val>num:
        return 0
     if num%val==0:
        return 1+Prime(num,val+1)
     else:
        return 0+Prime(num,val+1)
def Palindrome(num,place):
    if num==0:
        return 0
    return (num%10)*place+Palindrome(num//10,place//10)
def Palyprime(num):
    place=10**(len(str(num))-1)
    if Prime(num)==2 and Palindrome(num,place)==num:
            return 'palyprime'
    return 'not palyprime'
num=131
print(Palyprime(num))'''

#reverse
'''def Reverse(num,place):
    if num==0:
        return 0
    return (num%10)*place+Reverse(num//10,place//10)
num=415
place=10**(len(str(num))-1)
print(Reverse(num,place))'''

#strong
'''def factorial(num):
    if num<0:
        return 'not possible'
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
def strong(num):
    if num==0:
        return 0
    return factorial(num%10)+strong(num//10)
num=145
if strong(num)==num:
    print('strong')
else:
    print('not strong')'''

#fascinating
'''def fascinating(res,val=1):
    if val==10:
        return 'fascinating'
    if str(val) not in res:
        return 'not fascinating'
    return fascinating(res,val+1)
num=192
res=str(num*1)+str(num*2)+str(num*3)
print(fascinating(res))'''

#happy number
'''def Sq(num):
    if num==0:
        return 0
    return (num%10)**2+Sq(num//10)
def Happy(num):
    if num>9:
        num=Sq(num)
        return Happy(num)
    if num==7 or num==1:
        return 'happy number'
    return 'not happy number'
num=13
print(Happy(num))'''

'''def sq(num):
    if num==0:
        return 0
    return (num%10)**2+sq(num//10)
def happy(num):
    if num>9:
        num=sq(num)
        return happy(num)
    if num==7 or num==1:
        return 'happy num'
    return 'not happy number'
num=13
print(happy(num))'''

#terinary operator
#syntax:-val1 if cond else val2
num=10
print('even' if num%2==0 else 'odd') 

    




