def checkYear(year):
    import calendar
    return(calendar.isleap(year)) 
year = 2023
if (checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")
        

