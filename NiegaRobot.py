import mbot2, event, time, cyberpi

@event.is_press('a')
def is_btn_press():
    mbot2.servo_set(20,"S1")
    mbot2.servo_set(130,"S2")
    mbot2.servo_set(90,"S3")
    mbot2.servo_set(120,"S4")
    time.sleep(1)
    mbot2.forward(10, 2)
    time.sleep(1)
    mbot2.servo_set(20,"S1")
    for count in range(14):
        mbot2.servo_add(4,"S1")
        time.sleep(0.4)

    mbot2.servo_set(20,"S1")
    time.sleep(0.5)
    mbot2.turn(110)
    mbot2.servo_set(90,"S4")
    for count2 in range(7):
        mbot2.servo_set(120,"S3")
        time.sleep(0.3)
        mbot2.servo_set(60,"S3")
        time.sleep(0.3)

    mbot2.turn(-110)
    mbot2.servo_set(35,"S2")
    time.sleep(1)
    for count3 in range(17):
        mbot2.servo_add(4,"S1")
        time.sleep(0.1)

    mbot2.servo_set(110,"S2")
    cyberpi.stop_all()
