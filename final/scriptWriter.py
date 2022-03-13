config = ["nmos_on","nmos_off","pmos_on","pmos_off"]
Width = [1,2,3,4,6,8]
for zz in range(0,4):
	for yy in range(0,6):
		f = open(config[zz]+"/W"+str(Width[yy])+".sp",'w')
		f.write("*"+config[zz] + " Width = "+str(Width[yy]) + '''
.include 45nm_MGK.pm
.param LAMBDA = 22.5n
.global gnd

*mosfet description
M1 D G S B ''' + config[zz][:4]+" W={2*LAMBDA*" +str(Width[yy]) + "} L={2*LAMBDA}")
		if config[zz][0] == "n":
			f.write('''
Vb B gnd 0 
Vs S gnd 0
Vg G gnd 0
Vd D gnd 0

*dc sweep to change input parameters
				''' )
		else:
			f.write('''
Vb B gnd 1.2 
Vs S gnd 1.2
Vg G gnd 1.2
Vd D gnd 1.2

*dc sweep to change input parameters
				''' )
		if config[zz][-1] == "n":
			f.write('''
.dc Vg 0 1.2 .01''')
		else:
			f.write('''
.dc Vd 0 1.2 .01''')
		f.write('''

*control block
.control
set wr_singlescale
run
wrdata ''' + config[zz]+"/W"+str(Width[yy])+".txt "+'''v(d) v(g) v(s) v(b) (vd#branch) (vg#branch) (-vs#branch) (-vb#branch)
exit
.endc''')
		f.close()
