"""PlanB"""
def main():
    """chackscore"""
    num = int(input())
    if num >= 450:
        return pas()
    else:
        return fail()
def pas():
    """num>450"""
    print("Pass \nProcess is terminated")
def fail():
    """num<450"""
    print("Fail \nProcess is terminated")
main()
