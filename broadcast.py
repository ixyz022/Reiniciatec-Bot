import cyberpi 

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

@cyberpi.event.is_press("a")
def andar():
    while True:
        cyberpi.mbot2.forward(50, 2)
        cyberpi.mbot2.turn(90, 50)