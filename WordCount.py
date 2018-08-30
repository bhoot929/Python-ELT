ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""

Array_string = ss.split()

dict_words = {}.fromkeys(Array_string,0)
print(dict_words)
for words in Array_string:
    dict_words[words] += 1

print(dict_words)

''' Output:
{'I': 0, 'figured': 0, 'it': 0, 'out': 0, 'from': 0, 'black': 0, 'and': 0, 'white': 0, 'Seconds': 0, 'hours': 0, 'Maybe': 0, 'they': 0, 'had': 0, 'to': 0, 'take': 0, 'some': 0, 'time': 0}
{'I': 2, 'figured': 2, 'it': 2, 'out': 2, 'from': 1, 'black': 1, 'and': 2, 'white': 1, 'Seconds': 1, 'hours': 1, 'Maybe': 1, 'they': 1, 'had': 1, 'to': 1, 'take': 1, 'some': 1, 'time': 1}
'''
