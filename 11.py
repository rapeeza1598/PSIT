""" TheFunctionWithin """

def main():
    """ call function """
    aff = float(input())
    bff = float(input())
    cff = float(input())
    dff = float(input())
    answer1 = f_ofa(f_ofa(aff))
    print(answer1)


def f_ofa(num):
	""" equation 1 """
	numx = num*2
	return numx

def g_ofa(num):
	""" equation 2 """
	numx = 3*(num**4) - (num**3) + 2*(num**2) + 10
	return numx

