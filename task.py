from time import strptime
from datetime import datetime

romanian={}
result=[]
last_name= input("Введите вашу фамилию (заглавными латинскими буквами): ").upper()
FirstName = input("Введите ваше имя (заглавными латинскими буквами): ").upper()
gender = input("Введите ваш пол (либо 'm', либо 'w'): ")
birth = datetime.strptime(input("Введите вашу дату рождения(ДД-ММ-ГГ): "), "%d-%m-%Y")
city_string = input("Место рождения: ")
resident = input("Являетесь ли вы резедентом Румынии?: ")
if len(gender)!= 1:
    print("Неккоректный ввод данных!")
if len(city_string) != 2:
    print("Неккоректный ввод данных!")

    #Первая цифра

if birth.year>=1900 and birth.year<=1949:
    result.append(1)
    print(result)
elif birth.year>=1950 and birth.year<=1999:
    result.append(2)
    print(result)
elif birth.year>=1800 and birth.year<=1849:
    result.append(3)
    print(result)
elif birth.year>=1850 and birth.year<=1899:
    result.append(4)
    print(result)
elif birth.year>=2000 and birth.year<=2049:
    result.append(5)
    print(result)
elif birth.year>=2050 and birth.year<=2099:
    result.append(6)
    print(result)
if resident==True:
    result.append(7)
    print(result)
elif  resident == False:
    print(result)

    #Вторые 2 цифры

birth_str=str(birth.year)
last_two_digits = birth_str[-2:]
for i in last_two_digits:
    result.append(i)
print(result)
    #Третьи 2 цифры

birth_str_two=str(birth.month)
month_digits = birth_str_two[-2:]
for i in month_digits:
    result.append(i)

    #Четвертые 2 цифры

birth_str_three=str(birth.day)
day_digits = birth_str_three[-2:]
for i in day_digits:
    result.append(i)
print(result)






