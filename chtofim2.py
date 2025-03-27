# hostages=חטופים

#יבוא ספריה של תאריכים
from datetime import datetime

file1=open("hostages.txt",'a')
try:
    filetemp=open(file="hostages.txt",mode='r',encoding='utf-8')
    # print(filetemp.read())
except IOError as e:
    print(f"An error occurred while opening the file for appending: {e}")

hostages = [
    {"name": "אריאל ביבס", "nameToDaven": "אריאל בן שירי", "counter": 0},
    {"name": "שירי ביבס", "nameToDaven": "שירי בת מרגלית", "counter": 0},
    {"name": "כרמל גת", "nameToDaven": "כרמל בת כנרת", "counter": 0},
    {"name": "עומר ונקרט", "nameToDaven": "עומר בן ניבר", "counter": 0},
    {"name": "כפיר ביבס", "nameToDaven": "כפיר בן שירי", "counter": 0},
    {"name": "נעמה לוי", "nameToDaven": "נעמה בת איילת", "counter": 0},
    {"name": "טל שוהם", "nameToDaven": "טל בן ניצה", "counter": 0},
    {"name": "עומר שם טוב", "nameToDaven": "עומר בן שלי", "counter": 0},
    {"name": "דניאלה גלבוע", "nameToDaven": "גניאלה בת אורלי", "counter": 0},
    {"name": "אלון אהל", "nameToDaven": "אלון בן עידית", "counter": 0},
    {"name": "אבינתן אור", "nameToDaven": "אבינתן בן דיצה תרצה", "counter": 0},
    {"name": "יצחק אלגרט", "nameToDaven": "יצחק בן חנה", "counter": 0},
    {"name": "קארינה ארייב", "nameToDaven": "קארינה בת אירה", "counter": 0},
    {"name": "יגב בוכשטב", "nameToDaven": "יגב בן אסתר", "counter": 0},
    {"name": "ירדן ביבס", "nameToDaven": "ירדן בן פנינה", "counter": 0},
    {"name": "אגם ברגר", "nameToDaven": "אגם בת מירב", "counter": 0},
    {"name": "זיו ברמן", "nameToDaven": "זיו בן תמר", "counter": 0},

]

dayToDaven=['ראשון','שני','שלישי','רביעי','חמישי','שישי','שבת']
# dayToDaven=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

tempDayToDaven=dayToDaven.copy()        #העתקה של הימים לתהילים

emountBookToDaven=0
countBook=lambda emountBookToDaven:emountBookToDaven+1    #פונקציה שמעלה את כמות הספרי תהילים שנאמרו
# emountBookToDaven=countBook

#פונקציית להדפסת כל נתוני כל החטופים
def print_All_hostages():
    for i in hostages:
        print(i)

#פונקציית להדפסת שמות כל החטופים
def print_name_hostages():
    print('שמות כל החטופים שיחזרו בקרוב בעז"ה')
    for i in hostages:
        print(i['name'])

#פונקציה שמחזירה כמה ימים היו בשבי
def NumOfDaysOfCaptivity():
    startDay=datetime(2023, 10, 7)
    todey=datetime.now()
    daysOfCaptivity=(todey-startDay).days
    return daysOfCaptivity


# פונקציה ששולחים שם לתפילה וממקבלים יום לתהילים +כמה אנשים מתפללי םעל אותו חטוף ומעדכנת את הכמות המתפללים
def name_to_davening(otherName):
    num_days = NumOfDaysOfCaptivity()
    for i in hostages:
        if i['name'] == otherName:
            i['counter'] += 1
            print('\n', "name: ", i['name'], " name to daven: ", i['nameToDaven'], '\n',
                  " emount people davening to this person: ", i['counter'])
            print("thanks that you daven about: ", i['name'])
            print("day to daven: ", tempDayToDaven[0])
            print("The current date is: ",datetime.now())
            print(f"The number of days {i["name"]} in captivity are: ",num_days)
            del (tempDayToDaven[0])
            chckBook(tempDayToDaven)
            break
    else:
        print("this person is not a hostage")


#פונקציה שמקבלת יום בתהילים לומר ומוחקת מהמערך את היום הזה
def day_to_davening(myDay):
    if myDay in dayToDaven:
        index=[i for i in range(len(tempDayToDaven)) if tempDayToDaven[i]==myDay]
        if index:
            print("thanks that you say day {} in tailim day: ".format(tempDayToDaven[index[0]]))
            del (tempDayToDaven[index[0]])
            chckBook(tempDayToDaven)
        else:
            print("this day enother peouple say please you can take anothr day?")
    else:
        print("its not day")


# פונקציה שבודקת האם יש צורך בלפתוח ספר תהילים חדש
#אם כן גם מדפיסה כמה ספרים קראו כבר
def chckBook(tempDayToDaven):
    global emountBookToDaven
    if not tempDayToDaven:
        emountBookToDaven = countBook(emountBookToDaven)
        print(f"Empunt book that finish: {emountBookToDaven}")
        tempDayToDaven[:] = dayToDaven[:]
    else:
        print("")

#כמה ספרים נגמרו
def print_emount_Book_Finish():
    print("emount_Book_Finish", emountBookToDaven)
#איזה ימים נשארו
def print_Days_left_in_this_book():
    print("Days left from the current book",tempDayToDaven)

print(filetemp.read())
print("\n")
print_name_hostages()
print("\n")
print("אנו נשמח אם תוכל להוות חלק מהמיזם לאמירת תהילים לשובם של החטופים")
print("למיקרא שתרצה לעצור ולא להמשיך לקבל על עצמך עוד ימים לחץ סתופ")

# print_Days_left_in_this_book()
# print_emount_Book_Finish()
# #
# name_to_davening("שירי ביבס")
# name_to_davening("שירי ביבס")