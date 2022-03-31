from operator import itemgetter
import time
list = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}, {'name':'Apple', 'age':23}, {'name':'Destory', 'age':99}]
newlist = sorted(list, key=lambda d: d['age'])
print(newlist)


matrix = [ [4,5,6], [1,2,3], [7,0,9]]

sorted(matrix, key=itemgetter(1))
str = "012345"
print(str[3:3])
print(time.time())
print(1648729060819)
print(time.ctime(1647580087))
print(time.ctime(1648729060819/1000))