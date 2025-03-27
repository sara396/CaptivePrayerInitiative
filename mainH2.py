import chtofim2

name=input("enter name")
while(name!='סתופ'):
    chtofim2.name_to_davening(name)
    name=input("enter name")

day=input('enter day')
while(day!='סתופ'):
    chtofim2.day_to_davening(day)
    day = input('enter day')
print("תודה שאתה עוזר לנו להחזרת החטופים🙏🙏🙏")

    #למיקרה שאתה רוצה לדעת את שמות כל החטופים כתוב:
#chtofim2.print_name_hostages():
    #למיקרה שאתה רוצה לדעת את כל הפרטים על החטופים כתוב:
#chtofim2.print_All_hostages()
    #למיקרה שאתה רוצה לדעת את הימים שנשארו מהספר תהילים הפתוח כרגע כתוב:
#chtofim2.print_Days_left_in_this_book()
    #בשביל להתפלל על חולה מסוים כתוב:
# chtofim2.name_to_davening("שירי ביבס")
    #בשביל להתפלל יום מסוים בתהילים כתוב:
# chtofim2.day_to_davening('שישי')
    #בשביל לדעת כמה ספרי תהילים כבר נאמרו כתוב:
#chtofim2.chckBook(chtofim1.tempDayToDaven,chtofim1.emounBookToDaven)

