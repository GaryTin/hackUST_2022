from operator import itemgetter

list = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}, {'name':'Apple', 'age':23}, {'name':'Destory', 'age':99}]
newlist = sorted(list, key=lambda d: d['age'])
print(newlist)


matrix = [ [4,5,6], [1,2,3], [7,0,9]]

sorted(matrix, key=itemgetter(1))