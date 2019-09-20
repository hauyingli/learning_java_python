# birth_year =input("birth year: ")
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)
import datetime

now = datetime.date.today()
name = "date {}"
name_time = name.format(now)
print(name_time)