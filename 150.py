import math as m

ang = float(input("\ndigite angulo em graus "))

rang = ang * m.pi / 180

if((rang > m.pi/2 and rang <= m.pi) or (rang > 3*m.pi/2 and rang <= 2*m.pi)):
    print(" \nseno: ", m.sen(rang))
else:
    print(" \nco - seno: ", m.cos(rang))    
    