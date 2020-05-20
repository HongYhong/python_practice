def foo(s):
    n = int(s)
    assert n!=0 ,"it is zero"
    return 10/n
def main():
    foo('0')
main()