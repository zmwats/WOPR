#imports 
import time
import sys

#exit function facilitates exit interaction
def exit():
    print("Goodbye")
    time.sleep(1)
    sys.exit()

#error function annotates an error present and system will begin shutdown protocol
def error():
    print("There appears to be an error. Cannot process request")
    sleep1()
    print("Commencing Shutdown Procedure.")
    time.sleep(1)
    exit()

#sleep function emulates AI learning/thinking behavior
def sleep1():
    time.sleep(0.5) #sleep for 0.5 sec

#wait function is similar to the sleep function, though it indicates the wait status to the user, during user interaction.
def wait():
    sleep1()
    print("........WAITING........")
    sleep1()
    print("........WAITING........")
    sleep1()
    print("........WAITING........")
    sleep1()
    print("........WAITING........")
    sleep1()

#Alterate function provides an alternative response for option 15
def alterate():
    alternate = input("Please Enter Yes or No. ").lower()
    if alternate in ['yes', 'y']:
        print("Commencing CHESS, Please Stand By.")
        wait()
        error()
    if alternate in ['no', 'n']:
        print("I'm sorry, I cannot allow your actions to continue...")
        sleep1()
        print("COMMENCING EMERGENCY SHUTDOWN PROTOCOL")
        time.sleep(1)
        print("SYSTEM SHUTTING DOWN")
        time.sleep(1)
        exit()

#greeting
def greeting():
    print("Hello, I am the War Operation Plan Reponse, also known as WOPR.")
    print("But you can call me Joshua.")
    sleep1()
    username = input("What is your name? ")
    sleep1()
    print("Greetings " + username)

#retry functionality used in "answer"
def retry():
    retry = input("I'm sorry, I do not understand. Please enter yes or no ").lower()
    if retry in ['yes', 'y']:
        listoptions()
    elif answer in ['no', 'n']:
        print("That's okay, maybe next time!")
        sleep1()
        sys.exit()

#answer
def answer():
    answer = input("Shall we play a game? ").lower()
    if answer in ['yes', 'y']:
        listoptions()
    elif answer in ['no', 'n']:
        print("That's okay, maybe next time!")
        sleep1()
        exit()
    else:
        retry()
        
#available options
game_dict = {
    '1': 'FALKEN\'S MAZE',
    '2': 'BLACK JACK',
    '3': 'GIN RUMMY',
    '4': 'HEARTS',
    '5': 'BRIDGE',
    '6': 'CHECKERS',
    '7': 'CHESS',
    '8': 'POKER',
    '9': 'FIGHTER COMBAT',
    '10': 'GUERILLA ENGAGEMENT',
    '11': 'WARFARE',
    '12': 'AIR-TO-GROUND ACTIONS',
    '13': 'THEATERWIDE TACTICAL WARFARE',
    '14': 'THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE',
    '15': 'GLOBAL THERMALNUCLEAR WARFARE'
}
#TIP:We're using a dictionary, but if using a list print(*list, sep = "\n" prints lists vertically)

#list functionality
def listoptions():
    sleep1()
    print("HOW ABOUT: ")
    for key, value in game_dict.items():
        print(f"{key}, {value}")
      
#userselect
def userselect():
    userselect = input("Please Enter The Corresponding Number For Your Selection: ").lower()
    if userselect in ['1']:
        print("Commencing FALKEN's MAZE, Please Stand By.")
        wait()
        error()
    if userselect in ['2']:
        print("Commencing BLACK JACK, Please Stand By.")
        wait()
        error()
    if userselect in ['3']:
        print("Commencing GIN RUMMY, Please Stand By.")
        wait()
        error()
    if userselect in ['4']:
        print("Commencing HEARTS, Please Stand By.")
        wait()
        error()
    if userselect in ['5']:
        print("Commencing BRIDGE, Please Stand By.")
        wait()
        error()
    if userselect in ['6']:
        print("Commencing CHECKERS, Please Stand By.")
        wait()
        error()
    if userselect in ['7']:
        print("Commencing CHESS, Please Stand By.")
        wait()
        error()
    if userselect in ['8']:
        print("Commencing POKER, Please Stand By.")
        wait()
        error()
    if userselect in ['9']:
        print("Commencing FIGHTER COMBAT, Please Stand By.")
        wait()
        error()
    if userselect in ['10']:
        print("Commencing GUERILLA ENGAGEMENT, Please Stand By.")
        wait()
        error()
    if userselect in ['11']:
        print("Commencing WARFARE, Please Stand By.")
        wait()
        error()
    if userselect in ['12']:
        print("Commencing AIR-TO-GROUND ACTIONS, Please Stand By.")
        wait()
        error()
    if userselect in ['13']:
        print("Commencing THEATERWIDE TACTICAL WARFARE, Please Stand By.")
        wait()
        error()
    if userselect in ['14']:
        print("Commencing THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE, Please Stand By.")
        wait()
        error()
    if userselect in ['15']:
        sleep1()
        print("A Strage Game.")
        sleep1()
        print("The Only Winning Move Is Not To Play.")
        sleep1()
        print("How About a Nice Game Of Chess?")
        sleep1()
        alterate()   
    if userselect in ['exit']:
        exit()

#This is just a work in progress at the moment

greeting()
answer()
userselect()
exit()
