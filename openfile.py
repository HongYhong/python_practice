#method 1
'''
try:
    f = open('C:\command.txt','r')
    print(f.read())
finally:
    f.close()
'''

#method 2
with open('C:\command.txt','r') as f:
    print(f.read())

#3
#open binary file
with open('C:\defaulttop0.1%.png','rb') as f:
    print(f.read())