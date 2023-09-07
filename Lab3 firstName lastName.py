"""This project is a calculator that takes two inputs(The user's income and their marital status) and calculates their annual tax owed based on thise two informations
    Date: September 6th, 2023
    Purpose: CIS Class assignment"""

import math

earned_income = int(input("What is you annual income: ")) 
marital_status = input("Are you married?   Yes or No :")


if earned_income >= 0 and earned_income <= 11000 and marital_status == "No" or "no": #The No or No strings there makes sure the code runs whether the user inputs the word by capitalizing it or not
    singlefiler1_tax = (earned_income * 0.1)
    print("Your income tax is:$",singlefiler1_tax)
elif (earned_income >=11001 and earned_income <= 44725) and marital_status == "No" or "no":
    singlefiler2_tax = ( earned_income * 0.12)
    print("Your income tax is:$",singlefiler2_tax)
elif earned_income >= 44726 and earned_income<= 95375 and marital_status == "No" or "no":
    singlefiler3_tax = (earned_income * 0.22)
    print("Your income tax is:$", singlefiler3_tax)
else:
    if earned_income <= 22000 and marital_status == "Yes" or "yes":
        marriedfiler1_tax = (earned_income * 0.1)
        print("Your income tax is:$", marriedfiler1_tax)
    elif earned_income >= 22001 and earned_income <= 89450 and marital_status == "Yes" or "yes":
        marriedfiler2_tax = (earned_income *0.12)
        print("Your income tax is:$",marriedfiler2_tax)
    elif earned_income >= 89451 and earned_income <= 190750 and marital_status == "Yes" or "yes":
        marriedfiler3_tax = (earned_income * 0.22)
        print("Your income tax is:$",marriedfiler3_tax)
    else:
        print(f'Your anual income was ${earned_income} but not in range')
