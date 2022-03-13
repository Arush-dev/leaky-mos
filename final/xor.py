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

ff = open('xor.txt','w')
for zz in range(0,4):
	node = {}
	config = ["abn","zyn","ayp","zbp"]
	for yy in range(0,4):
		if yy in {0,1}:
			num = 2
		else: 
			num = 4
		f = open(str(config[yy])+"/W"+str(num)+".txt","r")
		f1 = f.readlines()
		f.close()
		node[yy] = float(f1[zz].split()[1])
		
	if zz == 0:
			I_sub = leak('p',4,'d',0,'s') + leak('p',4,'d',node[3],'s')
			I_gate = leak('p',4,'g',0,'s') + leak('p',4,'g',0,'d') + leak('p',4,'d',0,'g')
			I_gate = I_gate + leak('p',4,'d',node[3],'g') + 2*leak('n',2,'g',1.2,'d') + 2*leak('n',2,'g',1.2,'s')
			I_body = leak('p',4,'g',0,'b') + leak('p',4,'d',0,'b') + leak('p',4,'d',node[3],'b')
			I_body = I_body + 2*leak('n',2,'g',1.2,'b')

	if zz == 1:
			I_sub = leak('n',2,'d',1.2,'s') + leak('n',2,'d',node[1],'s')
			I_gate = 2*leak('p',4,'g',0,'s') + 2*leak('p',4,'g',0,'d') + 2*leak('p',4,'d',node[3],'g')
			I_gate = I_gate + leak('n',2,'d',1.2,'g') + leak('n',2,'g',1.2,'d') + leak('n',2,'g',1.2,'s')
			I_gate = I_gate + leak('n',2,'g',1.2-node[1],'s') + leak('n',2,'d',node[1],'g')
			I_body = 2*leak('p',4,'g',0,'b') + 2*leak('p',4,'d',node[3],'b') + leak('n',2,'d',1.2,'b')
			I_body = I_body + leak('n',2,'g',1.2,'b') + leak('n',2,'d',node[1],'b')

	if zz == 2:
			I_sub = leak('n',2,'d',1.2,'s') + leak('n',2,'d',node[0],'s')
			I_gate = 2*leak('p',4,'g',0,'s') + 2*leak('p',4,'g',0,'d') + 2*leak('p',4,'d',node[2],'g')
			I_gate = I_gate + leak('n',2,'d',1.2,'g') + leak('n',2,'g',1.2,'d') + leak('n',2,'g',1.2,'s')
			I_gate = I_gate + leak('n',2,'g',1.2-node[0],'s') + leak('n',2,'d',node[0],'g')
			I_body = 2*leak('p',4,'g',0,'b') + 2*leak('p',4,'d',node[2],'b') + leak('n',2,'d',1.2,'b')
			I_body = I_body + leak('n',2,'g',1.2,'b') + leak('n',2,'d',node[0],'b')

	if zz == 3:
			I_sub = leak('p',4,'d',node[2],'s') + leak('p',4,'d',0,'s')
			I_gate = leak('p',4,'g',0,'s') + leak('p',4,'g',0,'d') + leak('p',4,'d',0,'g')
			I_gate = I_gate + leak('p',4,'d',node[2],'g') + 2*leak('n',2,'g',1.2,'d') + 2*leak('n',2,'g',1.2,'s')
			I_body = leak('p',4,'d',node[2],'b') + leak('p',4,'g',0,'b') + leak('p',4,'d',0,'b')
			I_body = I_body + 2*leak('n',2,'g',1.2,'b')

	ff.write(str(zz)+" "+str(I_sub)+" "+str(I_gate)+" "+str(I_body)+"\n")

ff.close()
