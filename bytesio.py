from io import BytesIO
f = BytesIO()
f.write('语文'.encode('utf-8'))
print(f.getvalue())

t = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(t.read())