"""Timing II"""
def main():
    """kamnuntime"""
    num = int(input())
    seconds = num%60
    minutes = num//60
    minutes2 = minutes%60
    hours = num//3600
    hours2 = hours%24
    day = hours//24
    if num < 0:
        print("ERR_:__:__:__")
    elif day > 9999:
        print("ERR_:__:__:__")
    elif num >= 0:
        print("%04i:%02i:%02i:%02i" %(day, hours2, minutes2, seconds))
main()
