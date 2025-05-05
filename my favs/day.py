import re

month = {
    'jan': 0,
    'feb': 3,
    'mar': 3,
    'apr': 6,
    'may': 1,
    'jun': 4,
    'jul': 6,
    'aug': 2,
    'sep': 5,
    'oct': 0,
    'nov': 3,
    'dec': 5,
    '1': 0,
    '2': 3,
    '3': 3,
    '4': 6,
    '5': 1,
    '6': 4,
    '7': 6,
    '8': 2,
    '9': 5,
    '10': 0,
    '11': 3,
    '12': 5
}

monthNum = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    '11': 11,
    '12': 12
}

dayCodes = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

centuryCodes = {
    '17': 4,
    '19': 0,
    '18': 2,
    '20': 6
}

leapCode = 0


date = re.split(' / |/ | /|/| , | ,|, |,| ', re.sub(' +', ' ',input().strip()))

year = date[2]
YY = int(year[2:4])
yearCode = (YY + (YY//4)) % 7
monthCode = month[date[0].lower()[0:3]]

yearNum = int(year)

if yearNum >= 1752:
    if yearNum > 1752:
        cal = 'g'
    elif monthNum[date[0].lower()[0:3]] > 9:
        cal = 'g'
    elif monthNum[date[0].lower()[0:3]] == 9:
        if int(date[2]) >= 2:
            cal = 'g'
        else:
            cal = 'j'
    else:
        cal = 'j'   
else:
    cal = 'j'

if cal == 'g':
    num = yearNum
    while num > 2099:
       num = num - 400
    centuryCode = centuryCodes[str(num)[0:2]]

    if ((yearNum % 400 == 0) or ((yearNum % 4 == 0) and not(yearNum % 100 == 0))) and monthNum[date[0].lower()[0:3]] < 3:
        leapCode = 1
else:
    centuryCode = (18 - (yearNum // 100)) % 7
    if yearNum % 4 == 0 and monthNum[date[0].lower()[0:3]] < 3:
        leapCode = 1

day = dayCodes[(yearCode + monthCode + centuryCode + int(date[1]) - leapCode) % 7]

print(day)