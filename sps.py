import random
#Welcome
print("Welcome to the Rock,Paper,Scissor Game\n\t Are you ready?(y/n)")
ready=input("\t")
if ready=='y':
    print("\tGreat! Here we go..........\n\tEnter your name:")
    name=input("\t")
    if len(name)<3:
        print("Enter a valid name! :(")
        name=input("\tEnter your name:\n\t")
        if len(name)<3:
            print("Entered invalid name! :(\n*****Sorry try later*****")
            exit(0)
    else:
        print("Welcome \"" +name+"\" Good to see you")   
else:
    print(":| Okay, see you soon")
    exit(0)
#Section after name
print("Select '1' if you know how to play\nSelect '2' if you don't know how to play")
know=int(input())
if know==2:
    print('''This how to play:\nPress following keys:\nr --> Rock(r)\np --> Paper(p)\ns --> Scissor(s)''')
else:
    print('Hmmm, it seems you know the how to play:')
######game functions######
def start():    
    print("\t***The Game begins:***")
    print("Computer's turn\n select hidden :)))")
    r=random.randint(1,3)#comp turn
    if r==1:
        comp='r'
    elif r==2:
        comp='p'
    elif r==3:
        comp='s'

    you=input("Your turn:\n")
    p=game(comp,you)
    print(f"Computer select:{comp}\nYou select:{you}")
    result=gamewin(p)
    again=input("Want to play again?(y/n)")
    if again=='y':
        return start()
    else:
        print("Ok! See you later")
        exit(0)
def game(comp,you):
    if comp==you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False

def gamewin(p):
    if p== None:
        print("The game is tie :|")
    elif p:
        print("Congratulations! You won :)")
    else:
        print("Sorry! You Loss :(")



start()
