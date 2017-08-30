'''

gorpie - interest calculator
by Techett

'''


import time


p = input("What is the ammount you would like to calculate for? ")
t = input("How long will you be calculating for? ")
r = input("What is the rate of interest? ")
r = float(r)/100
a = int(p)*(1+float(r)*int(t))
print(a)


print()
print("Thank you!")
time.sleep(5)
