def countWords():
    f = input("enter the full flie name: ")
    file = open(f,"r")

    number = 0
    for i in file:
        words = i.split()
        number = number + len(words)
    
    print("the numbers of words in the file is: ")
    print(number)

countWords()
