import calendar


def getInput(prmpt, str, fin):
    while(True):
        try:
            value = input(prmpt)
            if value.lower() == 'exit':
                exit()
            if int(value) in range(str, fin+1):
                return int(value)
            else:
                raise ValueError
        except ValueError:
            print("That's not valid input, try again... \n")


def noDaysInMonYr(d, m, y):
    givenDay = 0
    for week in calendar.monthcalendar(y, m):
        if week[d] != 0:
            givenDay += 1
    return givenDay


print("--Day counter program--")
prompt = "Which day of the week do you want to count?\n" + \
    "0: Monday\n1: Tuesday\n2: Wednesday\n3: Thursday\n" + \
    "4: Friday\n5: Saturday\n6: Sunday\nOr 'exit' to quit\n? "
while(True):
    inDay = getInput(prompt, 0, 6)
    inYr = getInput("Enter year [0-3000]: ", 0, 3000)
    inMon = getInput("Enter month [1-12]: ", 1, 12)
    print("There are {} days of {} in the {} of {}.".format(
        noDaysInMonYr(inDay, inMon, inYr), calendar.day_name[inDay], calendar.month_name[inMon], inYr))
    print("-----------\n")
