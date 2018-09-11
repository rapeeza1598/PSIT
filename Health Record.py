"""Health Record"""
def main():
    """mainfunction"""
    data(1)
    data(2)
    data(3)
    data(4)
    data(5)
def data(num5):
    """mainfunction"""
    text = input()
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    print("** Patient No.%i **"%num5)
    print("Full Name: %s"%text)
    print("Birthday:  %i/%i/%i" %(num2, num3, num4))
    print("")
main()
