#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
md = Motor(Port.B)
mi = Motor(Port.C)
diametro_rueda = 55.5
distancia_entre_ruedas = 104
robot = DriveBase(md, mi, diametro_rueda, distancia_entre_ruedas)

ultrasonido = UltrasonicSensor(Port.S4)

velocidad=200
while True:
    distancia = ultrasonido.distance()
    mi.run(velocidad)
    md.run(velocidad)
    if(distancia <= 200 ):
        mi.stop()
        md.run_angle(500, 420)
 

    