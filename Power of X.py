"""Power of X"""
def main():
    """main"""
    num = int(input())
    num2 = num // 2
    for i in range(num2):
        print((' ' * i) + '\\' + (' ' * (num - 2)) + '/')
        num -= 2
    for j in range(num2-1, -1, -1):
        print((' ' * j) + '/' + (' ' * num) + '\\')
        num += 2
main()
