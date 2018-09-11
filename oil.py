""" TheFunctionWithin """

def main():
    """ call function """
    aff = float(input())
    bff = float(input())
    cff = float(input())
    dff = float(input())
    answer1 = f_of(f_of(aff))
    print(answer1)
    answer2 = g_of(f_of(aff - bff))
    print(answer2)
    answer3 = h_of(f_of(aff+bff), f_of(aff+cff), g_of(f_of(dff**2)))
    print(answer3)
    answer4 = i_of(h_of(f_of(aff + bff), f_of(aff - cff), g_of(f_of(dff**2)))\
, g_of(f_of(aff - bff)), f_of(f_of(f_of(f_of(f_of(cff))))), dff**8)
    print(answer4)

def f_of(num):
    """ equation 1 """
    numx = num*2
    return numx

def g_of(num):
    """ equation 2 """
    numx = 3*(num**4) - (num**3) + 2*(num**2) + 10
    return numx

def h_of(num1, num2, num3):
    """ equation 3 """
    numx = (num3 + num1)**2 - (num1*num2) + num2**2
    return numx

def i_of(num1, num2, num3, num4):
    """ equation 4 """
    part1 = (num1**2) + (num2**2) - (num3**2)
    part2 = (num4**2) - (2*num1*num4) + 2*num1
    numx = part1 / part2
    return numx
main()

