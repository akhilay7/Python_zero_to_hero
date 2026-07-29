from ast import Return


def 	TM_ion_concentration ():
   
    MW_TM = float(input('Molecular weight of Transition metal = MWTM = '))
    MW = float(input('Molecular weight = MW = '))
    P = float(input('Density = p = '))
    Ni = ((6.02214076) * (10^23) * (MW_TM) * (P)) / (MW)
    IID = pow((1 / (Ni)), 1 / 3)
    print("TM ion concentration = Ni = ", Ni)
    print("Inter ionic distance ri (Å) = ", IID)
    return Ni
 

TM_ion_concentration ()







