import os
import sys
sys.path[0:0] = [os.path.join(sys.path[0], '../examples/sat')]
import sat




Dorothy = 0
Virginia = 1
George = 2
Howard = 3

mena = ["Dorothy", "Virginia", "George", "Howard"]
zeny = [Dorothy,Virginia]
muzi = [George,Howard]



def otec(x):
    return x+1

def matka(x):
    return 4 + x + 1

def syn(x):
    return 8 + x + 1

def dcera(x):
    return 12 + x + 1

rola = ["otec", "matka", "syn", "dcera"]
def pribuzny(x,y):
    return 16 + 4*x + y + 1

def starsi(x,y):
    return 32 + 4*x + y + 1

def mladsi(x,y):
    return 48 + 4*x + y + 1

f1 = pribuzny(muzi[0], zeny[0])



with open("vstup.txt", "w") as f:
    #zeny nie su otec syn
    for o in zeny:
        f.write("{} 0 {} 0\n".format(-otec(o),-syn(o)))
    #muzi nie su matka dcera
    for m in muzi:
        f.write("{} 0 {} 0\n".format(-matka(m),-dcera(m)))
    
    for prem in [otec,syn]:
        #aspon jeden otec/syn
        for m in muzi:
            f.write("{} ".format(prem(m)))
        f.write("0 \n")
        #nie dvaja otcovia/synovia
        for m in muzi:
            f.write("{} ".format(-prem(m)))
        f.write("0 \n")

    
    #nesmie byt X zaroven otec aj syn
    for m in muzi:
        f.write("{} {} 0 \n".format(-otec(m),-syn(m)))        

        
    for prem in [matka,dcera]:
        #aspon jedna matka/dcera
        for m in zeny:
            f.write("{} ".format(prem(m)))
        f.write("0 \n")
        #nie dve matky/dcery
        for m in zeny:
            f.write("{} ".format(-prem(m)))
        f.write("0 \n")

    #nesmie byt X zaroven matka aj dcera
    for z in zeny:
        f.write("{} {} 0 \n".format(-matka(z),-dcera(z)))        

    #pokrvni pribuzni
    for m in muzi:
        for z in zeny:
            f.write("{} {} {} 0\n".format(-otec(m),dcera(z),pb(m,z)))
    for m in muzi:
        for m1 in muzi:
            if m != m1:
                f.write("{} {} {} 0\n".format(-otec(m),syn(m1),pb(m,m1)))
    for z in zeny:
        for z1 in zeny:
            if z != z1:
                f.write("{} {} {} 0\n".format(-matka(z),dcera(z1),pb(z,z1)))
    for m in muzi:
        for z in zeny:
            f.write("{} {} {} 0\n".format(-matka(z),syn(m),pb(z,m)))
    for m in muzi:
        for z in zeny:
            f.write("{} {} {} \n".format(-syn(m),-dcera(z),-pribuzny(m,z)))
            f.write("{} {} {} \n".format(-syn(m),-dcera(z),-pribuzny(m,z)))
            

    for m1 in muzi:
        for m2 in muzi:
            if m1!=m2:
                f.write("{} {} {} 0 \n".format(-otec(m1),-syn(m2),pribuzni(m1,m2)))
                f.write("{} {} {} 0 \n".format(-otec(m1),-syn(m2),pribuzni(m1,m2)))
            else:
                f.write("{} {} {} 0 \n".format(-otec(m1),-syn(m2),-pribuzni(m1,m2)))



s,ries = sat.SatSolver().solve("vstup.txt", "vystup.txt")

if not s:
    print("nema riesenie")
else:
    # dekodovanie riesenia
    for i in ries:
        if i > 0 and i < 17:
            i -= 1
            print("{}: {} \n".format(rola[i//4],mena[i%4]))
    
    
