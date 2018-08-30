#this code will count no of times word occurs in string:


def cal_occurance(str):
    dict = {}
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1
    return dict

print(cal_occurance('aabcccdefgghij'))

'''output:
{'a': 2, 'b': 1, 'c': 3, 'd': 1, 'e': 1, 'f': 1, 'g': 2, 'h': 1, 'i': 1, 'j': 1}
'''
