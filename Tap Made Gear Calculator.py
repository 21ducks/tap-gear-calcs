import math;

OD = 1
ODm = 1
ODM = 1
Cm = 1
CM = 1
P = 1
Z = 1
LA = 1
a = math.pi / 6

solve = 'x'

#Formulas:
# Cm = ZP
# Cm = pi ODm
# CM = pi ODM
# ODM = ODm + 2((P/2)/(tan(pi/6))
# ODm = Cm/pi
# OD = (ODM + ODm) / 2
# LA = P / (pi * OD)

print (" Variables: \n OD = Mean Outer Diameter \n ODm = Minor Diameter \n ODM = Major Diameter \n Cm = Minor circumference \n CM = Major Circumfere  \n P = Pitch of Tap \n Z = Number of Teeth \n LA = Lead Angle")
solve = input ("What are we solving for? ")
if solve == "Cm":
    #Cm = PZ
    Z = input ("How many teeth?")
    Z = int(Z)
    P = input ("What pitch teeth?")
    P = float(P)
    Cm = float(P*Z)
    print ("Cm = ")
    print (Cm)

elif solve == "P":
    #P = Cm/Z
    Z = input ("How many teeth?")
    Z = int(Z)
    Cm = input ("What minor circumference")
    Cm = float(Cm)
    P = float(Cm/Z)
    print ("P = ")
    print (P)    
elif solve == "Z":
    #P = Cm/Z
    P = input ("What pitch teeth?")
    P = float(P)
    Cm = input ("What minor circumference")
    Cm = float(Cm)
    Z = float(Cm/P)
    print ("Z = ")
    print (Z)
elif solve == "ODm":
    #ODm = Cm/pi = ZP/Pi
    Z = input ("How many teeth?")
    Z = int(Z)
    P = input ("What pitch teeth?")
    P = float(P)
    ODm = float((P*Z) / math.pi)
    print ("ODm = ")
    print (ODm)    
elif solve == "ODM":
    #ODM = ((P*Z)/Pi) + 2((P/2)/(tan(pi/6))
    Z = input ("How many teeth?")
    Z = int(Z)
    P = input ("What pitch teeth?")
    P = float(P) 
    ODM = float(((P*Z)/math.pi)+ (2*((P/2)/(math.tan(math.pi/6)))))
    print ("ODM = ")
    print (ODM)
elif solve == "OD":
    ODM = input ("What Major Diameter?")
    ODM = float(ODM)
    ODm = input ("What Minor Diameter?")
    ODm = float(ODm)
    OD = float ((ODM+ODm)/2)
    print ("OD = ")
    print (OD)
elif solve == "LA":
    OD = input ("What Mean Diameter?")
    OD = float(OD)
    P = input ("What Pitch Teeth?")
    P = int(P)
    LA = float (P/(OD*math.pi))
    print ("LA = ")
    print (LA)
    
