import random as ran
from pyfiglet import figlet_format as ff
import colorama
from colorama import Fore, Style, Back  
colorama.init(autoreset=True)
from emoji import emojize as emoji
rock_em = emoji(":rock:")
paper_em = emoji(":newspaper:")
scissors_em = emoji(":scissors:")
cpu_em = emoji(":laptop:")
check_em = emoji(":check_mark_button:")
person_em = emoji(":person:")
eq_em = emoji(":heavy_equals_sign:")
your_sc = 0
cpu_sc = 0
game_rounds = 5
# --------------------------------------------------------------------------------
print("")
print("")
print(Style.BRIGHT + "Welcome To ")
print("---------------------------------------------------------------")
print(Style.BRIGHT + Fore.BLUE + ff("Rock, Paper, Scissors", font="contessa"),"\r--------------")
print(Style.BRIGHT + Fore.RED + "by _-_ SAEED -_-")
print("-------------------------")
print("")
print("")
print(scissors_em,rock_em,paper_em," Press [s] to start the game or press [q] to quit the game: ",scissors_em,rock_em,paper_em,)
start = input()
print("")
cpu = ran.randint(1,3)
# Start Validation--------------------------------------------------------------------------------------------
while True:
    if start in ["q", "s"]:
        if start == "q":
            print(emoji(":waving_hand:")," Goodbye! Thanks for playing!")
            print("")
            break
        elif start == "s":
            print(Style.BRIGHT +Fore.GREEN + "//////////--------------------------------------------/////////")
            print("")
            print(emoji(":smiling_face_with_smiling_eyes:")," OK, Let's Play!")
            print("")
            print(person_em, f"Your Scores: {your_sc}")
            print(cpu_em,f"Computer Scores: {cpu_sc}")
            print("")
            print("Make your choice . . .",rock_em," ROCK (r)",paper_em, " PAPER (p)",scissors_em, " SCISSORS (s) : ")
            you = input()
            print("")  
            # Moves Validation---------------------------------------------------------------------------------
            while True:
                if you in ["r", "p", "s"]:
                    # CPU Rock move--------------------------------------------------------------------------------
                    if cpu == 1:
                        if you == 'r':
                            print("Computer Choice was also --",rock_em," ROCK --")
                            print(eq_em," SAME CHOICE!")
                            print("------------------------------")
                            print(person_em, f"Your Scores: {your_sc}")
                            print(cpu_em,f"Computer Scores: {cpu_sc}")
                            print("------------------------------")
                            break 
                       
                        elif you == 'p':
                            print("Computer Choice was --",rock_em," ROCK --")
                            print(check_em,person_em," YOU MADE A POINT !")
                            print("------------------------------")
                            your_sc += 1
                            print(person_em, f"Your Scores: {your_sc}")
                            print(cpu_em,f"Computer Scores: {cpu_sc}")
                            print("------------------------------")
                            break    
                       
                        elif you == 's':
                            print("Computer Choice was --",rock_em," ROCK --")
                            print(check_em,cpu_em," Computer MADE A POINT !")
                            print("------------------------------")
                            cpu_sc += 1
                            print(person_em, f"Your Scores: {your_sc}")
                            print(cpu_em,f"Computer Scores: {cpu_sc}")
                            print("------------------------------")
                            break
                      
                    # CPU Paper move--------------------------------------------------------------------------------
                    elif cpu == 2:
                        if you == 'r':
                            print("Computer Choice was --",paper_em," PAPER --")
                            print(check_em,cpu_em,"Computer MADE A POINT !")
                            print("------------------------------")
                            cpu_sc += 1
                            print(person_em, f"Your Scores: {your_sc}")
                            print(cpu_em,f"Computer Scores: {cpu_sc}")
                            print("------------------------------")
                            break 
                      
                        elif you == 'p':
                            print("Computer Choice was also --",paper_em," PAPER --")
                            print(eq_em," SAME CHOICE!")
                            print("------------------------------")
                            print(person_em, f"Your Scores: {your_sc}")
                            print(cpu_em,f"Computer Scores: {cpu_sc}")
                            print("------------------------------")
                            break     
                       
                        elif you == 's':
                            print("Computer Choice was --",paper_em,"PAPER --")
                            print(check_em,person_em,"YOU MADE A POINT !")
                            print("------------------------------")
                            your_sc += 1
                            print(person_em, f"Your Scores: {your_sc}")
                            print(cpu_em,f"Computer Scores: {cpu_sc}")
                            print("------------------------------")
                            break
                       
                    # CPU Scissors move--------------------------------------------------------------------------------
                    elif cpu == 3:
                        if you == 'r':
                            print("Computer Choice was --",scissors_em," SCISSORS --")
                            print(check_em,person_em,"YOU MADE A POINT !")
                            print("------------------------------")
                            your_sc += 1
                            print(person_em, f"Your Scores: {your_sc}")
                            print(cpu_em,f"Computer Scores: {cpu_sc}")
                            print("------------------------------")
                            break 
                      
                        elif you == 'p':
                            print("Computer Choice was --",scissors_em," SCISSORS --")
                            print(check_em,cpu_em,"Computer MADE A POINT !")
                            print("------------------------------")
                            cpu_sc += 1
                            print(person_em, f"Your Scores: {your_sc}")
                            print(cpu_em,f"Computer Scores: {cpu_sc}")
                            print("------------------------------")
                            break      
                        
                        elif you == 's':
                            print("Computer Choice was also --",scissors_em," SCISSORS --")
                            print(eq_em," SAME CHOICE!")
                            print("------------------------------")
                            print(person_em, f"Your Scores: {your_sc}")
                            print(cpu_em,f"Computer Scores: {cpu_sc}")
                            print("------------------------------")
                            break                                                         
                else:
                    print(Fore.RED+ Style.BRIGHT + "---- - - - - -  -  -  -  -  -   -   -   -   -   -  -  -  -  -  - - - - - -----")
                    print(emoji(":cross_mark:"),emoji(":expressionless_face:")," The Only Options available at this point are [r], [p] or [s]")
                    print("")
                    print("Make your choice . . .",rock_em," ROCK (r)",paper_em, " PAPER (p)",scissors_em, " SCISSORS (s) : ")
                    you = input()
                    print("")
            if cpu_sc or your_sc == game_rounds:
                break        

    
    
    else:
        print(Fore.RED+ Style.BRIGHT + "---- - - - - -  -  -  -  -  -   -   -   -   -   -  -  -  -  -  - - - - - -----")
        print(emoji(":no_entry:"),emoji(":thinking_face:")," Only [s] to start or [q] to quit")
        print("")
        print(scissors_em," Press [s] to start the game or press [q] to quit the game: . . .",scissors_em)
        start = input()
        print("")      
# --------------------------------------------------------------------------------------------------------------------
        
