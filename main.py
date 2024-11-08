from cat import Cat
given_name=input("What would you like to name your cat")
given_colour=input("What colour would you like your cat to be?")
while True:
    option=input("What would you like to do with your cat? 1.Play 2.Train 3.Feed 4.Sleep 5.Stats")
    if option=="1":
        given_name.play()
    elif option=="2":
        given_name.train()
    elif option=="3":
        given_name.feed()
    elif option=="4":
        given_name.sleep()
    else:
        given_name.stats()
        

