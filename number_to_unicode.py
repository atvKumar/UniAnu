# -*- coding: utf-8 -*-
from math import floor

def numberTounicode(number):
    # 1 - 19
    ones = ['சுழியம்', 'ஒன்று', 'இரண்டு', 'மூன்று', 'நான்கு', 'ஐந்து', 'ஆறு',
            'ஏழு', 'எட்டு', 'ஒன்பது', 'பத்து', 'பதினொன்று', ' பனிரண்டு',
            'பதிமூன்று', 'பதினான்கு', 'பதினைந்து', 'பதினாறு', 'பதினேழு',
            'பதினெட்டு', 'பத்தொன்பது']
    # 20 - 90
    tens = [' ', ' ', 'இருபது', 'முப்பது', 'நாற்பது', 'ஐம்பது', 'அறுபது',
            'எழுபது', 'எண்பது', 'தொன்னூறு']
    # 20 - 90
    tens_suffix = [' ', ' ', 'இருபத்தி', 'முப்பத்தி', 'நாற்பத்தி', 'ஐம்பத்தி', 'அறுபத்தி',
                   'எழுபத்தி', 'எண்பத்தி', 'தொன்னூற்றி']
    # 100 - 900
    hrds = [' ', 'நூறு', 'இரு நூறு', 'முன்னூறு', 'நாநூறு', 'ஐநூறு',
            'அறுநூறு', 'எழுநூறு', 'எண்ணூறு', 'தொள்ளாயிரம்']
    # 100 - 900
    hrds_suffix = [' ', 'நூற்றி', 'இருநூற்றி', 'முன்னூற்று', 'நாநூற்று', 'ஐநூற்று',
                   'அறுநூற்று', 'எழுநூற்று', 'எண்ணூற்று', 'தொள்ளாயிரத்து']

    def two_digits(inp):
        if inp < 20:
            return ones[inp]
        elif inp >= 20 and inp % 10 == 0:
            return tens[inp/10]
        else:
            x = int(floor(inp/10))
            y = inp % 10
            z = tens_suffix[x] + ' ' + ones[y]
            return z

    def three_digits(inp):
        if inp < 100:
            return two_digits(inp)
        if inp % 100 == 0:
            return hrds[inp/100]
        else:
            x = int(floor(inp/100))
            z = hrds_suffix[x] + ' ' + two_digits(int(str(inp)[1::]))
            return z

    def four_digits(inp):
        x = int(floor(inp/1000))
        if inp == 1000:
            return "ஓர் ஆயிரம்"
        if inp % 1000 == 0 and inp != 1000:
            return ones[x] + " ஆயிரம்"
        else:
            if inp > 1000 and inp < 2000:
                return "ஆயிரத்தி " + three_digits(int(str(inp)[1::]))

    def five_digits(inp):
        x = int(floor(inp/1000))
        if inp % 1000 == 0:
            return two_digits(x) + " ஆயிரம்"
        else:
            return two_digits(x) + " ஆயிரம் " + three_digits(int(str(inp)[2::]))

    def six_digits(inp):
        x = int(floor(inp/100000))
        if inp % 100000 == 0:
            if x == 1:
                return "ஒரு இலட்சம்"
            else:
                return ones[x] + " இலட்சம்"
        else:
            y = int(str(inp)[1::])
            if y > 999:
                if x == 1:
                    return "ஒரு இலட்சத்தி "+ five_digits(int(str(inp)[1::]))
                else:
                    return ones[x] + " இலட்சத்தி " + five_digits(int(str(inp)[1::]))
            elif y > 99:
                if x == 1:
                    return "ஒரு இலட்சத்தி " + three_digits(y)
                else:
                    return ones[x] + " இலட்சத்தி " + three_digits(y)
            else:
                if x == 1:
                    return "ஒரு இலட்சத்தி " + two_digits(y)
                else:
                    return ones[x] + " இலட்சத்தி " + two_digits(y)

    def seven_digits(inp):
        x = int(floor(inp/100000))
        if inp % 100000 == 0:
            return two_digits(x) + " இலட்சம்"
        else:
            y = int(str(inp)[1::])
            if y > 999:
                return two_digits(x) + " இலட்சத்தி " + five_digits(int(str(inp)[2::]))
            elif y > 99:
                return two_digits(x) + " இலட்சத்தி " + three_digits(y)
            else:
                return two_digits(x) + " இலட்சத்தி " + two_digits(y)

    def eight_digits(inp):
        x = int(floor(inp/10000000))
        if inp % 10000000 == 0:
            if x == 1:
                return "ஒரு கோடி"
            else:
                return ones[x] + " கோடி"
        else:
            y = int(str(inp)[1::])
            if y > 999:
                if x == 1:
                    return "ஒரு கோடியே " + seven_digits(int(str(inp)[1::]))
                else:
                    return ones[x] + " கோடி"+ seven_digits(int(str(inp)[1::]))
            elif y > 99:
                if x == 1:
                    return "ஒரு கோடியே " + three_digits(y)
                else:
                    return ones[x] + " கோடி " + three_digits(y)
            else:
                if x == 1:
                    return "ஒரு கோடியே " + two_digits(y)
                else:
                    return ones[x] + " கோடி " + three_digits(y)


    strNum = str(number)

    if len(strNum) == 1 or len(strNum) == 2:
        # Two Digit Numbers
        return unicode(two_digits(number), 'utf-8')
    if len(strNum) == 3:
        # Three Digit Numbers
        return unicode(three_digits(number), 'utf-8')
    if len(strNum) == 4:
        # Four Digit Numbers
        return unicode(four_digits(number), 'utf-8')
    if len(strNum) == 5:
        # Five Digit Numbers
        return unicode(five_digits(number), 'utf-8')
    if len(strNum) == 6:
        # Six Digit Numbers
        return unicode(six_digits(number), 'utf-8')
    if len(strNum) == 7:
        # Seven Digit Numbers
        return unicode(seven_digits(number), 'utf-8')
    if len(strNum) == 8:
        # Eight Digit Numbers
        return unicode(eight_digits(number), 'utf-8')