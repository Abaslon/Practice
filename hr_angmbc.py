import math as m

AB=int(input())
BC=int(input())

MC =  m.sqrt( ((AB*AB) + (BC*BC) ) /2)

BM = m.sqrt( (BC*BC) + (MC*MC) )

angMBC= m.acos( ( (BM*BM)+(BC*BC)-(MC*MC) ) / (2*BM*BC) )

angMBCf=int(round(angMBC))

print(angMBCf)