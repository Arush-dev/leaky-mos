config = ["abn","zyn","zbp","ayp","abn_and"]
width = [1,2,3,4,6,8]

for zz in range(0,5):
	for yy in range(0,6):
		for xx in range(0,4):
			f = open(config[zz]+"/W" + str(width[yy]) + "_"+str(xx)+".sp",'w')
			f.write(str(config[zz])+" " +str(width[yy])+" "+str(xx)+" "+
'''
.include 45nm_MGK.pm
.param LAMBDA=22.5n
.global vdd gnd
V0 vdd gnd 1.2''')
			if zz == 0:
				if xx == 0:
					f.write('''
V1 ud gnd 0
V2 ug gnd 0
V3 us dd 0
V4 ub us 0 
V5 dg gnd 0
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
				if xx == 1:
					f.write('''
V1 ud gnd 1.2
V2 ug gnd 0
V3 us dd 0
V4 ub us 0 
V5 dg gnd 1.2
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
				if xx == 2:
					f.write('''
V1 ud gnd 1.2
V2 ug gnd 1.2
V3 us dd 0
V4 ub us 0 
V5 dg gnd 0
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
				if xx == 3:
					f.write('''
V1 ud gnd 0
V2 ug gnd 1.2
V3 us dd 0
V4 ub us 0 
V5 dg gnd 1.2
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
			if zz == 1:
				if xx == 3:
					f.write('''
V1 ud gnd 0
V2 ug gnd 0
V3 us dd 0
V4 ub us 0 
V5 dg gnd 0
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
				if xx == 2:
					f.write('''
V1 ud gnd 1.2
V2 ug gnd 0
V3 us dd 0
V4 ub us 0 
V5 dg gnd 1.2
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
				if xx == 1:
					f.write('''
V1 ud gnd 1.2
V2 ug gnd 1.2
V3 us dd 0
V4 ub us 0 
V5 dg gnd 0
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
				if xx == 0:
					f.write('''
V1 ud gnd 0
V2 ug gnd 1.2
V3 us dd 0
V4 ub us 0 
V5 dg gnd 1.2
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
			if zz == 2:
				if xx == 0:
					f.write('''
V1 us gnd 1.2
V2 ug gnd 1.2
V3 ud ds 0
V4 ub us 0 
V5 dg gnd 0
V6 dd gnd 0
V7 db ds 0 
M1 ud ug us ub pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
						''')
				if xx == 1:
					f.write('''
V1 us gnd 1.2
V2 ug gnd 1.2
V3 ud ds 0
V4 ub us 0 
V5 dg gnd 1.2
V6 dd gnd 0
V7 db ds 0 
M1 ud ug us ub pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
						''')
				if xx == 2:
					f.write('''
V1 us gnd 1.2
V2 ug gnd 0
V3 ud ds 0
V4 ub us 0 
V5 dg gnd 0
V6 dd gnd 1.2
V7 db ds 0 
M1 ud ug us ub pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
						''')
				if xx == 3:
					f.write('''
V1 us gnd 1.2
V2 ug gnd 0
V3 ud ds 0
V4 ub us 0 
V5 dg gnd 1.2
V6 dd gnd 0
V7 db ds 0 
M1 ud ug us ub pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
						''')
			if zz == 3:
				if xx == 3:
					f.write('''
V1 us gnd 1.2
V2 ug gnd 1.2
V3 ud ds 0
V4 ub us 0 
V5 dg gnd 0
V6 dd gnd 0
V7 db ds 0 
M1 ud ug us ub pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
						''')
				if xx == 2:
					f.write('''
V1 us gnd 1.2
V2 ug gnd 1.2
V3 ud ds 0
V4 ub us 0 
V5 dg gnd 1.2
V6 dd gnd 0
V7 db ds 0 
M1 ud ug us ub pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
						''')
				if xx == 1:
					f.write('''
V1 us gnd 1.2
V2 ug gnd 0
V3 ud ds 0
V4 ub us 0 
V5 dg gnd 0
V6 dd gnd 1.2
V7 db ds 0 
M1 ud ug us ub pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
						''')
				if xx == 0:
					f.write('''
V1 us gnd 1.2
V2 ug gnd 0
V3 ud ds 0
V4 ub us 0 
V5 dg gnd 1.2
V6 dd gnd 0
V7 db ds 0 
M1 ud ug us ub pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db pmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
						''')
			if zz == 4:
				if xx == 0:
					f.write('''
V1 ud gnd 1.2
V2 ug gnd 0
V3 us dd 0
V4 ub us 0 
V5 dg gnd 0
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
				if xx == 1:
					f.write('''
V1 ud gnd 1.2
V2 ug gnd 0
V3 us dd 0
V4 ub us 0 
V5 dg gnd 1.2
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
				if xx == 2:
					f.write('''
V1 ud gnd 1.2
V2 ug gnd 1.2
V3 us dd 0
V4 ub us 0 
V5 dg gnd 0
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
				if xx == 3:
					f.write('''
V1 ud gnd 0
V2 ug gnd 1.2
V3 us dd 0
V4 ub us 0 
V5 dg gnd 1.2
V6 ds gnd 0 
V7 db gnd 0 
M1 ud ug us ub nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
M2 dd dg ds db nmos W={2*LAMBDA*'''+str(width[yy])+'''} L={2*LAMBDA}
''')
# **************************************************************************
			f.write('''
.dc V0 1.2 1.2 1.2
.control 
set appendwrite
run
wrdata '''+str(config[zz])+"/W"+str(width[yy]))
			if zz in {2,3}:
				f.write(".txt V(ud)\n")
			else:
				f.write(".txt V(dd)\n")
			f.write('''
exit
.endc''')
