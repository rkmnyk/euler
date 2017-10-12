
# TODO: looks like a non-functional version
def compute():

    date = 1
    month = 1
    year = 1900
    day = 1
    count = 0


    while True:
        if((year == 2020)):
            break

        #if sunday, reset day, if first sunday, increase counter
        if day == 7:
            day=1
        else:
            day+=1

        #30 day months
        if((month == 9) or (month == 4) or (month ==6) or (month == 11)):
            if date == 30:
                date = 1
                month += 1
            else:
                date += 1

        #31 day months
        elif((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10)):
            if date == 31:
                date = 1
                month += 1
            else:
                date += 1

        #february
        elif month == 2:
            if date == 28:
                if(year % 4 == 0):
                    if(year % 100 == 0):
                        if(year % 400 == 0):
                            date += 1
                        else:
                            date = 1
                            month += 1
                    else:
                        date += 1
                else:
                    month+=1
                    date = 1
            elif date == 29:
                month+=1
                date=1
            else:
                date += 1

        #december
        elif month == 12:
            if date == 31:
                date = 1
                month = 1
                year += 1
            else:
                date+=1


        if((date == 13) and (day == 5) and (year == 2017)):
            count+=1

    return count

if __name__== "__main__":
    print(compute())
