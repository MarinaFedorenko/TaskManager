import datetime

today = datetime.datetime.now()
currentMonth = today.month
currentYear = today.year

print(today)
print(currentMonth)
print(currentYear)
#
# selectYear = document.getElementById("year")
# selectMonth = document.getElementById("month")
#
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


#
# monthAndYear = document.getElementById("monthAndYear")
# showCalendar(currentMonth, currentYear)
#
#
def next():
    # currentYear = self.currentYear
    # if currentMonth==11:
    #     self.currentYear+=1
    #     currentMonth= (currentMonth+1)%12
    # showCalendar(currentMonth, currentYear)
    print("Я в next()")
    pass


#
#
def previous():
    #     currentYear = (currentMonth == 0) ? currentYear - 1 : currentYear
    #     currentMonth = (currentMonth == 0) ? 11 : currentMonth - 1
    #     showCalendar(currentMonth, currentYear)
    print("Я в previos()")
    pass
#
#
# def jump():
#     currentYear = parseInt(selectYear.value)
#     currentMonth = parseInt(selectMonth.value)
#     showCalendar(currentMonth, currentYear)
#
#
# def showCalendar(day, month, year):
#
#     firstDay = (new Date(year, month)).getDay()
#     daysInMonth = 32 - new Date(year, month, 32).getDate()
#
#     tbl = document.getElementById("calendar-body") # body of the calendar
#
#     # clearing all previous cells
#     tbl.innerHTML = ""
#
#     #filing data about month and in the page via DOM.
#     monthAndYear.innerHTML = months[month] + " " + year
#     selectYear.value = year
#     selectMonth.value = month
#
#     # creating all cells
#     date = 1
#     for (let i = 0; i < 6; i++) :
#         # creates a table row
#          row = document.createElement("tr")
#
#         #creating individual cells, filing them up with data.
#         for (let j = 0; j < 7; j++):
#             if (i === 0 && j < firstDay) :
#                 cell = document.createElement("td")
#                 cellText = document.createTextNode("")
#                 cell.appendChild(cellText)
#                 row.appendChild(cell)
#
#                  else if (date > daysInMonth) :
#                     break
#
#
#             else :
#                 cell = document.createElement("td")
#                 cellText = document.createTextNode(date)
#                 if (date === today.getDate() && year === today.getFullYear() && month === today.getMonth()):
#                     cell.classList.add("bg-info");
#                 # color today's date
#                 cell.appendChild(cellText)
#                 row.appendChild(cell)
#                 date++
#
#
#
#
#
#         tbl.appendChild(row); # appending each row into calendar body.

