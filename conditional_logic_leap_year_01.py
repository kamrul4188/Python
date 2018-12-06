#conditional logic Leap year 01


year = input ("Please enter year : ")

if year %4 != 0:
    print year,  "is not a leap year"
else:
    if year %100 == 0:
        if year %400 == 0:
            print year, "is a leap year"
        else:
            print year, "is not a leap year"
    else:
        print year, "is a leap year"
