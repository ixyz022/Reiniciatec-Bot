import cyberpi 
import pygame
import time

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Bandera para el estado de cada tecla
key_up = False
key_down = False
key_left = False
key_right = False

# Bucle principal
running = True
while running:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Se presionó la barra espaciadora.")
                print(cyberpi.quad_rgb_sensor.get_line_sta(index = 1))
                for i in range(3):
                    print(cyberpi.ultrasonic2.get(index = 1))
            elif event.key == pygame.K_UP:
                key_up = True
            elif event.key == pygame.K_DOWN:
                key_down = True
            elif event.key == pygame.K_LEFT:
                key_left = True
            elif event.key == pygame.K_RIGHT:
                key_right = True
            elif event.key == pygame.K_x:
                cyberpi.mbot2.servo_set(180, 1)
                time.sleep(2)
                cyberpi.mbot2.servo_set(0, 1)
                
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key_up = False
            elif event.key == pygame.K_DOWN:
                key_down = False
            elif event.key == pygame.K_LEFT:
                key_left = False
            elif event.key == pygame.K_RIGHT:
                key_right = False

    # Realizar acciones según el estado de cada tecla
    if key_up:
        print("Se está presionando la flecha hacia arriba.")
        cyberpi.mbot2.forward(100)
    elif key_down:
        print("Se está presionando la flecha hacia abajo.")
        cyberpi.mbot2.backward(100)
    elif key_left:
        print("Se está presionando la flecha hacia la izquierda.")
        cyberpi.mbot2.turn_left(100)
    elif key_right:
        print("Se está presionando la flecha hacia la derecha.")
        cyberpi.mbot2.turn_right(100)
    else: 
        cyberpi.mbot2.forward(0)
    # Actualizar pantalla
    pygame.display.flip()

# Salir de pygame
pygame.quit()
