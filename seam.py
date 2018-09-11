def main():
    A = ['a','b','c']
    A.insert(1,1)
    A.append(3)
    print(A)
    y = A.index('b')
    A.insert(y+1,2)
    print(A)
    #e = A.pop(5)
    #print(e)
    x = A.pop(len(A)-3)
    print(x)
    print(A)
main()