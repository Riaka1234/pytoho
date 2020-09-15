Pa=int(35)
Pb= float(19.9)
año= int(0)
while Pb<Pa:

    Pb=Pb*1.03
    Pa=Pa*1.02
    año=año+1
print('poblacion a= ',Pa,', poblacion b= ',Pb)
print('año en el cual la poblacion b es mayor que la a ',año)
