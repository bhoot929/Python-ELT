# The greatest common multiple (GCF) of two numbers
# is the smallest positive integer that is perfectly
# divisible by the two given numbers.
def GCF_Funct(x, y):
    if x > y:

        lesser = y
    else:

        lesser = x
    num = lesser

    hcf = 0

    for i in range(1,num + 1):

        if (x%i == 0 and  y%i == 0):
            hcf = i


    return hcf


num1 = 54
num2 = 24
print('The HCF of', num1, 'and', num2, 'is', GCF_Funct(num1, num2))

'''output: The HCF of 54 and 24 is 6'''
