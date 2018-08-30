# The least common multiple (L.C.M.) of two numbers
# is the smallest positive integer that is perfectly
# divisible by the two given numbers.

def LCM_Funct(x,y):
    if x > y:
        greater = x
        lesser = y
    else:
        greater = y
        lesser = x
    num = greater
    num = x*y
    lcm = 0

    for i in range(num+1):

            if((i+lesser)%x ==0 and (i+lesser)%y==0):
                    lcm = i+lesser
                    break;



    return lcm

num1 = 7
num2 = 9
print('The LCM of', num1, 'and', num2, 'is' , LCM_Funct(num1,num2))
