
print(''''
 ____  ____  ____  ____  _  _  ____  ____    _  _  _  _  __ _  ____
(_  _)(  _ \(  __)/ ___)/ )( \(  _ \(  __)  / )( \/ )( \(  ( \(_  _)
  )(   )   / ) _) \___ \) \/ ( )   / ) _)   ) __ () \/ (/    /  )(  
 (__) (__\_)(____)(____/\____/(__\_)(____)  \_)(_/\____/\_)__) (__) 
 ''')
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
******************************************************************************* 

 ''')
print('''Hi, I am genie 🧞 of Treasure Island 
I am bound to this island
There is only one rule:
# Win the trasure at all cost
You have to answer set of questions to reach the treasure
If you do not choose answers from option, you will be trapped in the island forever
Lets begin ''')
print('1. There are two ways. One leads to jungle and other leads to caves. Enter "jungle" to move in jungle and "cave" to move towarsds cave')
a=input()
if a=="jungle":
    print('A dragon came and defeated you. Game Over !!!')
elif a=="cave":
    print('2. Inside one big cave there are three cave entrances. First one is blue, second one is green and third one is red. Enter "1" to move in first cave, "2" to enter in second cave and "3" to enter in third cave. Enter your choice')
    a=input()
    if a=="1":
        print('🌋There is a fire pit. Game Over')
    elif a=="2":
        print('🕳 There is a spike pit. Game Over')
    elif a=="3":
        print('3. 🏃 There is now a skeleton in front of you. It is having a scroll in its hand. Enter "yes" to take the scroll or "no" to run away ')
        a=input()
        if a=="no":
            print("☠ A skeleton army came after you. Game Over ☠")
        elif a=="yes":
            print('4. 📜 The scroll is containing the direction towards the treasure. Enter "left" to move left or "right" to move right. Enter your choice')
            a=input()
            if a == "left":
                print('⛰ You fell in a cliff. Game Over')
            elif a=="right":
                print('5. 💰Now the treasure is on a rock surrounded by water. Enter "yes" to move forward by boat or "no" to swim towards the treasure. Enter your choice')
                a=input()
                if a =="yes":
                    print('🧟There was a zombie in the boat. Game over')
                elif a=="no":
                    print('🎉🎉🎉🎉🎉🎉🎉🎉\nYou have won the Game\nCongratulations!!!\nNow the genie is liberated.\n🎉🎉🎉🎉🎉🎉🎉🎉')
                else:
                    print('🚫🚫🚫You have entered wrong option.Now you are trapped in island as genie. Game Over🚫🚫🚫')
            else:
                print('🚫🚫🚫You have entered wrong option.Now you are trapped in island as genie. Game Over🚫🚫🚫')
        else:
            print('🚫🚫🚫You have entered wrong option.Now you are trapped in island as genie. Game Over🚫🚫🚫')
    else:
        print('🚫🚫🚫You have entered wrong option.Now you are trapped in island as genie. Game Over🚫🚫🚫')

else:
    print('🚫🚫🚫You have entered wrong option.Now you are trapped in island as genie. Game Over🚫🚫🚫')


