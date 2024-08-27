import random 

rock=('''
         ___.--"          "\'.         
  ------f"               // \\\        
        |                    |||       
        |                    |||    
    ----L_-XXX-.             .|'    
                "\   -<_____///     
                  \___)     -"''')

paper=('''___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' ''')

scissor=('''.-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/''')

game_image=[rock,paper,scissor]

user_choice=int(input("what do you want to choose?0 for rock,1 for paper,2 for scissor: "))
print(game_image[user_choice])

computer_choice=random.randint(0,2)
print("computer choice: ")
print(game_image[computer_choice])

if user_choice==0 and computer_choice==2:
    print("you win!")
elif user_choice>=3:
    print("invalid no.")
elif computer_choice==0 and user_choice==2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif computer_choice == user_choice:
    print("draw") 