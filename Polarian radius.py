def 	Polaron_radius ():
    π=22/7
    Ni = float(input('TM ion concentration =  Ni = '))
    Polaron_rad = (1 / 2) * pow((π /(6 * (Ni))), 1 / 3)
    print("Polaron radius rp (Å)  = ", Polaron_rad)

Polaron_radius()