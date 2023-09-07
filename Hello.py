
""" This lab takes place on the planet Pythoid where everything is exactly the same as Earth, except that all months have exactly 30 days.
    Date: 08/31/2023
    Title: Calculating Dog and cat age
    Author: Rahimatu Yushawu#
"""
import math


age = float(input("How old are you?")) #Take the age of the user

dog_age = (age * 7) #converts age to dog age without the decimal place
years = (dog_age // 1)  #runs the dog age of humans
month = (dog_age % 1 * 12 // 1) #converts fractional years to months
days = (dog_age % 1 * 12 % 1 * 30 // 1) #converts the fractional years to days

#This section calculates in cat years

cat_age = (age / 9) #converts age to cat age without the decimal place
years_1 = (cat_age // 1)  #runs the cat age of humans
month_1 = (cat_age % 1 * 12 // 1) #converts fractional years to months
days_1 = (cat_age % 1 * 12 % 1 * 30 // 1) #converts the fractional years to days

#This section calculates in horse years

horse_age = 3*((age ** 2 - 47) / 7 + 12) #converts age to horse age without the decimal place
years_2 = (horse_age // 1)  #runs the horse age of humans
month_2 = (horse_age % 1 * 12 // 1) #converts fractional years to months
days_2 = (horse_age % 1 * 12 % 1 * 30 // 1) #converts the fractional years to days

print(horse_age)
print(f' Your dog age in years is {years} {month} months and {days} days')

print(f' Your cat age in years is {years_1} {month_1} months and {days_1} days')

print(f' Your horse age in years is {years_2} {month_2} months and {days_2} days')











