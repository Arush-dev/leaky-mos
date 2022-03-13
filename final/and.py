def leak(mos,width,flag,volts,curr):
    file_dest = ""
    if mos == "n":
        file_dest = file_dest + "nmos_"
    elif mos == "p":
        file_dest = file_dest + "pmos_"
    if flag == "d":
        file_dest = file_dest + "off"
    elif flag == "g":
        file_dest = file_dest + "on"
    file_dest = file_dest + "/W" + str(width) + ".txt"
    mos_model = open(file_dest,"r")
    val = mos_model.readlines()
    mos_model.close()
    val = val[round(float(volts)*100)]
    val = val.split()
    if curr == "d":
        return abs(float(val[5]))
    elif curr == "g":
        return abs(float(val[6]))
    elif curr == "s":
        return abs(float(val[7]))
    elif curr == "b":
        return abs(float(val[8]))

ff = open('and.txt','w')
for zz in range(0,4):
    f = open("abn_and/W2.txt","r")
    f1 = f.readlines()
    f.close()
    node = f1[zz].split()[1]
    node = float(node)
    if zz == 0:
        I_sub = leak('n',2,'d',node,"s") + leak('p',2,'d',0,"s")
        I_gate = leak('n',1,'g',1.2,"d") + leak('n',1,'g',1.2,"s") + 2*leak('n',2,'d',node,'g')
        I_gate = I_gate + leak('n',2,'d',1.2,'g') + leak('p',2,'d',0,'g') + 2*leak('p',2,'g',0,'s')
        I_gate = I_gate + 2*leak('p',2,'g',0,'d')
        I_body = 2*leak('p',2,'g',0,'b') + leak('p',2,'d',0,'b') + leak('n',1,'g',1.2,'b')
        I_body = I_body + leak('n',2,'d',node,'b') + leak('n',2,'d',1.2-node,'b')

    if zz == 1:
        I_sub = leak('n',2,'d',1.2-node,'s') + leak('p',2,'d',0,'s')
        I_gate = 2*leak('p',2,'g',0,'d') + leak('p',2,'d',0,'g') + leak('n',1,'g',1.2,'s')
        I_gate = I_gate + leak('n',1,'g',1.2,'d') + leak('n',2,'d',1.2,'g') + leak('n',2,'g',1.2,'d')
        I_gate = I_gate + leak('n',2,'g',1.2,'s')
        I_body = leak('p',2,'g',0,'b') + leak('p',2,'d',0,'b') + leak('n',1,'g',1.2,'b')
        I_body = I_body + leak('n',2,'g',1.2,'b') + leak('n',2,'d',1.2-node,'b')

    if zz == 2:
        I_sub = leak('n',2,'d',node,'s') + leak('p',2,'d',0,'s')
        I_gate = leak('p',2,'g',0,'s') + leak('p',2,'g',0,'d') + leak('p',2,'d',0,'g')
        I_gate = I_gate + leak('n',1,'g',1.2,'d') + leak('n',1,'g',1.2,'s') + leak('n',2,'d',node,'g')
        I_body = leak('p',2,'g',0,'b') + leak('p',2,'d',0,'b') + leak('n',2,'d',node,'b')
        I_body = I_body + leak('n',1,'g',1.2,'b')

    if zz == 3:
        I_sub = 2*leak('p',2,'d',0,'s') + leak('n',1,'d',1.2,'s')
        I_gate = 2*leak('p',2,'d',0,'g') + leak('p',2,'g',0,'s') + leak('p',2,'g',0,'d')
        I_gate = I_gate + leak('n',1,'d',1.2,'g') + 2*leak('n',2,'g',1.2,'d')
        I_gate = I_gate + 2*leak('n',2,'g',1.2,'s')
        I_body = 2*leak('p',2,'d',0,'b') + 2*leak('n',2,'g',1.2,'b') + leak('p',2,'g',0,'b')
        I_body = I_body + leak('n',1,'d',1.2,'b')
    
    ff.write(str(zz)+" "+str(I_sub)+" "+str(I_gate)+" "+str(I_body)+"\n")

ff.close()
