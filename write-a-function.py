def is_leap(year):
    leap =  True if year%4==0 else False if year%100==0 and year%400==0 else False
    return leap