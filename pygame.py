import random 
print( "   ____  ___  _   _____  ____   _        _____     " )
print( "  /  __\ \  \//  /  __/ /  _ \ / \__/| /  __/    " )
print( "  |  \/|  \  /   | |  _ | / \| | |\/|| |  \      " )
print( "  |  __/  / /    | |_// | |-|| | |  || |  /_     " )
print( "  \_/    /_/     \____\ \_/ \| \_/  \| \____\    " )
                                     
wining_num = random.randint(1,10)
if input("type 'exit' to quit the game : type enter to continue :  ----->>>> "):
        exit
guess = 1
num = int(input("player ---> 1 <---  Enter a number between 1 to 10 :"))
num2= int(input("player ---> 2 <---  Enter an other  number 1 to 10 :"))
game_over = False
while True:
    if num == wining_num:
        print(f"congress player ---> 1 <--- you won and you guessed the number {guess} times ! ")
        print("*********************Game Over*********************")
        break
    else:
        if num < wining_num:
            print(" player 1 : number is too low")
        else:
            print(" player 1 : number is too high")
    if num2 == wining_num:
         print(f"congress player ---> 2 <--- you won and you guessed the number {guess} times ! ")
         print("*********************Game Over*********************")
         break
    else:
        if num2 < wining_num:
            print(" player 2 : number is too low")
        else:
            print(" player 2 : number is too high")
        guess += 1     
        num = int(input(" guess again player ---> 1 :"))
        num2= int(input(" guess again player ---> 2 :"))
    


