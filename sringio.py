from io import StringIO
f = StringIO('hello\nworld\nabc')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

