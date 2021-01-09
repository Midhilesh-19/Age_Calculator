import datetime

birth_year = int(input("Enter your birth year =")) #enter your birth year
age = datetime.datetime.now().year - birth_year
'''datetime.now.year indicates present year from the system default
and then substract the given year from current year'''

print("Your age is ",age,"years old")
