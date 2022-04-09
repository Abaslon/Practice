def is_leap(y):
    if y%4==0 and y%100 !=0:
        return True
    elif y%4==0 and y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        return False
    
is_leap(int(input()))
