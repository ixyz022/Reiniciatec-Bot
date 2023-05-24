import cyberpi 
import time 

def bloque_inicial():
    r2 = cyberpi.quad_rgb_sensor.get_color_sta(1, 1)
    l2 = cyberpi.quad_rgb_sensor.get_color_sta(4, 1)
    if r2 == "green" and l2 == "red":
        cyberpi.console.print("logrado")
        
def reconocer_color():
    rojo1 = cyberpi.quad_rgb_sensor.get_red(1, 1)
    rojo2 = cyberpi.quad_rgb_sensor.get_red(2, 1)
    rojo3 = cyberpi.quad_rgb_sensor.get_red(3, 1)
    rojo4 = cyberpi.quad_rgb_sensor.get_red(4, 1)
    cyberpi.console.print("r1:")
    cyberpi.console.println(rojo1)
    cyberpi.console.print("r2:")
    cyberpi.console.println(rojo2)
    cyberpi.console.print("r3:")
    cyberpi.console.println(rojo3)
    cyberpi.console.print("r4:")
    cyberpi.console.println(rojo4)
    
def filtrar_color(rojo, verde, azul):
    if rojo < 0 or rojo > 255 or verde < 0 or verde > 255 or azul < 0 or azul > 255:
        return "Los valores de color deben estar entre 0 y 255."
    
    if rojo > verde and rojo > azul:
        return "El color es rojo."
    elif verde > rojo and verde > azul:
        return "El color es verde."
    elif azul > rojo and azul > verde:
        return "El color es azul."
    elif rojo == verde == azul:
        return "El color es gris."
    else:
        return "El color es una combinación de colores."
    
def rojo(index):
    cyberpi.quad_rgb_sensor
    
def fijar_color_leds(): 
    cyberpi.quad_rgb_sensor.set_led("w", 1)

@cyberpi.event.is_press("a")
def callback():
    cyberpi.quad_rgb_sensor.off_led(1)
    time.sleep(1)
    fijar_color_leds()
    while True: 
        reconocer_color()
        
@cyberpi.event.is_press("b")
def callback2(): 
    filtrar_color()