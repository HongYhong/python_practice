from io import StringIO
from io import BytesIO
def outputstring():
    return 'abc\nhong\nfox'
s = outputstring()
sio = StringIO()
sio.write(s)
sio.seek(20,0)
print(sio.tell())

bio = BytesIO()
bio.write(s.encode('utf-8'))
print(bio.getvalue())
bio.seek(-11,1)
print(bio.tell())
for i in bio.readlines():
    print(i.strip())