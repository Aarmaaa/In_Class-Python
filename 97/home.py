intro = input("enter your introduction: ")
print(intro)
words = 1
charthers = 0

for i in intro:
    charthers = charthers + 1
    if(i == " "):
        words = words + 1

print("number of words in the intro :" )
print(words)

print("number of charthers in the intro: ")
print(charthers)

# Notes:
#   

# for(var i = 0;i=>10;i--)

#for/in loop

""" for (var i in array){}

[40, 50, 60, 70]
i = 0, 1, 2, 3

i = 40, 50, 60, 70 """