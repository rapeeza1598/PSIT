"""Four Dots"""
import math
def main(numx2, nunx1, numy2, numy1):
    """mainfunction"""
    num = math.sqrt((numx2-nunx1)**2+(numy2-numy1)**2)
    return num
def data():
    """mainfunction"""
    numxa = int(input())
    numya = int(input())
    numxb = int(input())
    numyb = int(input())
    numxc = int(input())
    numyc = int(input())
    numxd = int(input())
    numyd = int(input())
    pointa = main(numxa, numxb, numya, numyb)
    pointb = main(numxb, numxc, numyb, numyc)
    pointc = main(numxc, numxd, numyc, numyd)
    pointd = main(numxd, numxa, numyd, numya)
    num2 = pointa+pointd+pointc+pointb
    print("%.2f"%num2)
data()
