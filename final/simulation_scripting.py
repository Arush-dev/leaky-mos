def nmos(num,W,drain,gate,source,body):
    sr = "M" + str(num) + " "
    dd = "d" + str(num) + " "
    gg = "g" + str(num) + " "
    ss = "s" + str(num) + " "
    bb = "b" + str(num) + " "
    sr = sr + dd + gg + ss + bb + "nmos W={2*LAMBDA*" + str(W) + "} L={2*LAMBDA}\nV" + dd + dd +drain +" 0\nV" + gg + gg + gate + " 0\nV" + ss +ss + source +" 0\nV"
    sr = sr + bb + bb+ body + " 0\n"
    return sr

def pmos(num,W,drain,gate,source,body):
    sr = "M" + str(num) + " "
    dd = "d" + str(num) + " "
    gg = "g" + str(num) + " "
    ss = "s" + str(num) + " "
    bb = "b" + str(num) + " "
    sr = sr + dd + gg + ss + bb + "pmos W={2*LAMBDA*" + str(W) + "} L={2*LAMBDA}\nV" + dd + dd +drain +" 0\nV" + gg + gg + gate + " 0\nV" + ss +ss + source +" 0\nV"
    sr = sr + bb + bb+ body + " 0\n"
    return sr

def ad(a,b,n):
    y = "u" + str(n)
    z = "d" + str(n) 
    v  = "o" + str(n)
    s = "vdd"
    g = "gnd"
    x = pmos(100*n+1,2,y,a,s,s) + pmos(100*n+2,2,y,b,s,s) + nmos(100*n+3,2,y,a,z,z) + nmos(100*n+4,2,z,b,g,g) + pmos(100*n+5,2,v,y,s,s) + nmos(100*n+6,1,v,y,g,g)
    return x

def nt(a,b,n):
    x = pmos(100*n+1,2,b,a,'vdd','vdd') + nmos(100*n+2,1,b,a,'gnd','gnd')
    return x

def xr(a,b,n):
    bb = 'bb' + str(n)
    ab = 'ab' + str(n)
    x = nt(a,ab,11) + nt(b,bb,12)
    node = ["ul" +str(n), "ur" + str(n) , "dl" + str(n) , "dr" + str(n),"o" + str(n)]
    s = "vdd"
    g = "gnd"
    n = 100*n
    x = x + pmos(n+1,4,node[0],a,s,s) + pmos(n+2,4,node[4],bb,node[0],node[0]) + pmos(n+3,4,node[1],ab,s,s) + pmos(n+4,4,node[4],b,node[1],node[1])
    x = x + nmos(n+5,2,node[4],a,node[2],node[2]) + nmos(n+6,2,node[2],b,g,g) + nmos(n+7,2,node[4],ab,node[3],node[3]) + nmos(n+8,2,node[3],bb,g,g)
    return x


netlist = "\n.include 45nm_MGK.pm\n.param LAMBDA={22.5n}\n.global vdd gnd\nV0 vdd gnd 1.2\n\n"
g = open('temp.txt','r')
g1 = g.readlines()
g.close()
a1,a0 = g1[0].split()
b1,b0 = g1[1].split()
mult = ad('a0','b0',1) + ad('a0','b1',2) + ad('a1','b0',3) + ad('a1','b1',4) + xr('o2','o3',5)
mult = mult + ad('o2','o3',6) + xr('o4','o6',7) + ad('o4','o6',8)

if a1 is 1.2:
    a1 = "Va1 a1 gnd 1.2"
else:
    a1 = "Va1 a1 gnd 0"
if a0 is 1.2:
    a0 = "Va0 a0 gnd 1.2"
else:
    a0 = "Va0 a0 gnd 0"
if b1 is 1.2:
    b1 = "Vb1 b1 gnd 1.2"
else:
    b1 = "Vb1 b1 gnd 0"
if b0 is 1.2:
    b0 = "Vb0 b0 gnd 1.2"
else:
    b0 = "Vb0 b0 gnd 0"

wrdatag = "wrdata simulation.txt "
wrdatab = wrdatag
for xx in range(1,9):
    if xx in {5,7}:
        for tt in range(1,9):
            wrdatag = wrdatag +"Vg" + str(xx*100 + tt) + "#branch "
            wrdatab = wrdatab +"Vb" + str(xx*100 + tt) + "#branch "
    else:
        for tt in range(1,7):
            wrdatag = wrdatag +"Vg" + str(xx*100 + tt) + "#branch "
            wrdatab = wrdatab +"Vb" + str(xx*100 + tt) + "#branch "

netlist = netlist + a0 + "\n" + a1 + "\n" + b0 + "\n" + b1 + "\n" + mult + "\n.dc V0 1.2 1.2 1.2\n"
netlist = netlist + ".control\nset wr_singlsscale\nset appendwrite\nrun\n"+wrdatag+"\n"+wrdatab + "\nexit\n.endc\n"
f = open('simulation.sp','w')
f.write(netlist)
f.close()
