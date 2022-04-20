import random
loewer = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "123456789"
symbol = "{},[],#,(),*,;,_,-"

all = loewer + upper + NUMBER + symbol
length = 9 
password = "".join(random.sample(all,length))
print("The Pasword you genrated is : ",password)