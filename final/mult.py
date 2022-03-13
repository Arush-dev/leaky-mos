def leakage(gate,int1,int2):
    if int1 is 1:
        if int2 is 1:
            num = 3
        else:
            num = 2
    else:
        if int2 is 1:
            num = 1
        else:
            num = 0
    if gate == 'xor':
        f = open('xor.txt','r')
        f1 = f.readlines()[num]
        f.close()
        return f1.split()
    else:
        f = open('and.txt','r')
        f1 = f.readlines()[num]
        f.close()
        return f1.split()

def xor_gate(x,y):
    if x is not y:
        return 1
    else:
        return 0

def and_gate(x,y):
    if int(x) is 1:
        if int(y) is 1:
            return 1
        else:
            return 0
    else:
        return 0

a1,a0 = input("ENTER 1ST BINARY NUMBER: ")
b1,b0 = input("ENTER 2ND BINARY NUMBER: ")
g = open('temp.txt','w')
g.write(a1+" "+a0+'\n'+b1+" "+b0 + "\n")
c0 = and_gate(a0,b0)
i0 = and_gate(a0,b1)
#print(a0,b1,i0)
i1 = and_gate(a1,b0)
i2 = and_gate(a1,b1)
c1 = xor_gate(i0,i1)
i3 = and_gate(i0,i1)
c2 = xor_gate(i2,i3)
c3 = and_gate(i2,i3)
I_sub = float(leakage('and',a0,b0)[1]) + float(leakage('and',a0,b1)[1]) + float(leakage('and',a1,b0)[1])
I_sub = I_sub + float(leakage('and',a1,b1)[1]) + float(leakage('and',i0,i1)[1]) + float(leakage('and',i2,i3)[1])
I_sub = I_sub + float(leakage('xor',i0,i1)[1]) + float(leakage('xor',i2,i3)[1])
I_gate = float(leakage('and',a0,b0)[2]) + float(leakage('and',a0,b1)[2]) + float(leakage('and',a1,b0)[2])
I_gate = I_gate + float(leakage('and',a1,b1)[2]) + float(leakage('and',i0,i1)[2]) + float(leakage('and',i2,i3)[2])
I_gate = I_gate + float(leakage('xor',i0,i1)[2]) + float(leakage('xor',i2,i3)[2])
I_body = float(leakage('and',a0,b0)[3]) + float(leakage('and',a0,b1)[3]) + float(leakage('and',a1,b0)[3])
I_body = I_body + float(leakage('and',a1,b1)[3]) + float(leakage('and',i0,i1)[3]) + float(leakage('and',i2,i3)[3])
I_body = I_body + float(leakage('xor',i0,i1)[3]) + float(leakage('xor',i2,i3)[3])

#print(f"FIRST INPUT NUMBER: {a1}{a0}")
#print(f"SECOND INPUT NUMBER: {b1}{b0}")
#print(i0,i1,i2,i3)
print(f"OUTPUT: {c3}{c2}{c1}{c0}")
print(f"SUBTHRESHOLD LEAKAGE CURRENT: {I_sub}")
print(f"GATE LEAKAGE CURRENT: {I_gate}")
print(f"BODY LEAKAGE CURRENT: {I_body}")
e = open('out.txt','w')
e.write("\n\n\nOUTPUT: " + str(c3)+str(c2)+str(c1)+str(c0)+"\n\n\n")
e.close()
g.write(str(I_sub)+ " ")
g.write(str(I_gate)+ " ")
g.write(str(I_body)+"\n")
g.close()
