import os
import sys


L = []
misslist = []


def listdir(path, pattern):
    try:
        for f in os.listdir(path):
            if os.path.isdir(os.path.join(path, f)):
                listdir(os.path.join(path, f), pattern)
            else:
                if pattern in f:
                    L.append(os.path.join(path, f))
    except:
        misslist.append(os.path.join(path, f))


def main():
    try:
        pwd = os.path.abspath(sys.argv[1])
        pattern = sys.argv[2]
        listdir(pwd,pattern)
        print('pattern list:',L)
        print('missing list:',misslist)
    except Exception as e:
        print(e,'\nUsage:python findfile.py [path] [pattern]')

if __name__ == "__main__":
    main()
