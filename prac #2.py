'''
TSITSI NYAMHONDO 
H150323Z

'''

def num_chars(string1):
    dict = {}
    for n in string1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(num_chars('google.com'))
