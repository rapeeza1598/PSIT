"""DataSpike"""
def main():
    """chacknum"""
    data1 = int(input())
    data2 = functionchackdata(int(input()), data1)
    data3 = functionchackdata(int(input()), data2)
    data4 = functionchackdata(int(input()), data3)
    data5 = functionchackdata(int(input()), data4)
    data6 = functionchackdata(int(input()), data5)
    data7 = functionchackdata(int(input()), data6)
    data8 = functionchackdata(int(input()), data7)
    print(data8)
def functionchackdata(num1, num2):
    """chackdatainput"""
    if num1 > num2:
        return num1
    else:
        return num2
main()
