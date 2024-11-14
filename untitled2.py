# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SLeG-yJhX7buyefwzEdQwrK8tw7vRRch
"""

import pandas as pd
baza= {
    "FISH":[ "Yuldashev Muhammadyusuf", "Saminova Maxsudaxon", "Yuldasheva Muqaddasxon", "Raxmatov Bahodirjon", "Solijonov Muhammadamin", "Sultanov Fazliddin", "Bahodir Jalolov", "Maxmud Murodov", "Abbos Fayzullayev", "Shavkat Mirziyoyev" ],
    "Manzil":[ "Farg'ona tumani", "Farg'ona tumani", "Farg'ona tumani", "Quva tumani", "Beshariq tumani", "Namangan shaxri", "Samarqand", "Dushanbe", "Moskva", "Uzbekistan" ],
    "Yoshi":[  "19", "43", "17", "19", "19", "19", "30", "34", "21", "67" ],
    "Kasbi":[ "TATUFF talabasi", "20-maktab", "O'quvchi", "Bank direktori", "TATUFF talabasi", "TATUFF talabasi", "Bokschi", "MMA jangchisi", "Professional futbolchi", "Prezident" ],
    "Jinsi":[ "erkak", "ayol", "ayol", "erkak", "erkak", "erkak", "erkak", "erkak", "erkak", "erkak" ]
}
db=pd.DataFrame(baza)
print(db)

filtr1=db[db[ "Kasbi" ]=="TATUFF talabasi"]
print(filtr1)

filtr2=db[db["Jinsi"]=="ayol"]
print(filtr2)

filtr3=db[db["Yoshi"]>"19"]
print(filtr3)