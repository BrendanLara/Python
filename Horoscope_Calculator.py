# Add your solution to the problem "horoscope" here.

#  Implement a comparison function for dates
#
#  Returns true if the date (month1, day1) is
#  earlier in the calendar than (month2, day2).
#  Assumes the days are valid and doens't do any checking.
def before(month1, day1, month2, day2):
    if (month1 < month2):
        return True
    elif(month1 > month2):
        return False
    elif(month1 == month2):
        if(day1 < day2):
            return True
        else:
            return False

# Implement a sign function.
#
# Returns the sign for the given month and day, or
# "INVALID_DATE" if the date is not valid, e.g. month=10 day=54
# Must not print anything out.
def sign(month, day):

    if (month <= 0 or month > 12 or day <= 0):
        return 'INVALID_DATE'

    elif (month == 1):
        if (day > 31):
            return 'INVALID_DATE'
        elif (before(month, day, 1, 20) == True):
            return 'Capricorn'
        else:
            return 'Aquarius'


    elif (month == 2):
        if (day > 29):
            return 'INVALID_DATE'
        elif (before(month, day, 2, 19) == True):
            return 'Aquarius'
        else:
            return 'Pisces'

    elif (month == 3):
        if (day > 31):
            return 'INVALID_DATE'
        elif (before(month, day, 3, 21) == True):
            return 'Pisces'
        else:
            return 'Aries'

    elif (month == 4):
        if (day > 30):
            return 'INVALID_DATE'
        elif (before(month, day, 4, 20) == True):
            return 'Aries'
        else:
            return 'Taurus'

    elif (month == 5):
        if (day > 31):
            return 'INVALID_DATE'
        elif (before(month, day, 5, 21) == True):
            return 'Taurus'
        else:
            return 'Gemini'

    elif (month == 6):
        if (day > 30):
            return 'INVALID_DATE'
        elif (before(month, day, 6, 21) == True):
            return 'Gemini'
        else:
            return 'Cancer'

    elif (month == 7):
        if (day >31):
            return 'INVALID_DATE'
        elif (before(month, day, 7, 23) == True):
            return 'Cancer'
        else:
            return 'Leo'

    elif (month == 8):
        if (day > 31):
            return 'INVALID_DATE'
        elif (before(month, day, 8, 23) == True):
            return 'Leo'
        else:
            return 'Virgo'

    elif (month == 9):
        if (day > 30):
            return 'INVALID_DATE'
        elif (before(month, day, 9, 23) == True):
            return 'Virgo'
        else:
            return 'Libra'

    elif (month == 10):
        if (day > 31):
            return 'INVALID_DATE'
        elif (before(month, day, 10, 23) == True):
            return 'Libra'
        else:
            return 'Scorpio'

    elif (month == 11):
        if (day > 30):
            return 'INVALID_DATE'
        elif (before(month, day, 11, 22) == True):
            return 'Scorpio'
        else:
            return 'Sagittarius'

    elif (month == 12):
        if (day > 31):
            return 'INVALID_DATE'
        elif (before(month, day, 12, 22) == True):
            return 'Sagittarius'
        else:
            return 'Capricorn'

# Your main function should prompt the user for a month and day and
# print out the sign using return value of the sign function.
def main():
    month = int(input('What number month? '))
    day = int(input('What number day? '))

    print(sign(month,day))



# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
