from datetime import date

def diffInMonth(dateD, dateG):
	nb_month = (dateD.year - dateG.year)*12 + (dateD.month - dateG.month)
	nb_month -= 1 if dateG.day>dateD.day else 0
 
	return nb_month

begin = input().split('.')
end = input().split('.')

f_date=date(int(begin[2]),int(begin[1]),int(begin[0]))
l_date=date(int(end[2]),int(end[1]),int(end[0]))

delta=(l_date-f_date).days
delta_month=diffInMonth(l_date, f_date)

year = str(int(delta//365)) + " years, " if delta//365 > 1 else str(int(delta//365)) + " year, " if delta//365 > 0 else ""
month = str(int(delta_month%12)) + " months, " if delta_month%12 > 1 else str(int(delta_month%12)) + " month, " if delta_month%12 > 0 else ""

print("{}{}total {} days".format(year, month, delta))