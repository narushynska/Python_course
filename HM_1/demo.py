# make list flattern

def flatten_list(array):
    res = [int(s) for s in (str(array).replace('[', '').replace(']', '').split(','))]
    return res


list_old = [1, 2, 12, 3, 4, [3, 4], 4, 5, [[5, 6, 7, 8], 8], 9, 90, 75]

print flatten_list(list_old)


# check if parenthesis are balanced
def check_parenthesis_balanced(string):
    return string.count('(') == string.count(')')


string = '(((((2, 3))))))'
print 'Are parenthesis balanced? {ans}'.format(ans=check_parenthesis_balanced(string))
