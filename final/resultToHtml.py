config = ["nmos_on","nmos_off","pmos_on","pmos_off"]
Width = [1,2,3,4,6,8]
f1 = open('results.html','w')
f1.write('''<style>
main {
  display: flex;
  justify-content: center;
}
table {
  max-width: 100%; width: 75%;
}
tr:nth-child(odd) {
  background-color: #fff;
}
tr:nth-child(even) {
  background-color: #c6e4ee;
}
th {
  background-color: #03a9f4;
  color: #555;
}
th,
td {
  text-align: center;
  padding: 0.5em 1em;
	</style>''')
f1.write("<center>")
for zz in range(0,4):
	for yy in range(0,6):
		f = open(config[zz]+"/W"+str(Width[yy])+".txt",'r')
		f1.write("<h3>" + config[zz].upper() + " WIDTH = "+ str(Width[yy]).upper() +"</h3>"+
			'''<table border="1" style="border-collapse:collapse">
				<tr>
					<th>Vsupply</th>
					<th>Vdrain</th>
					<th>Vgate</th>
					<th>Vsource</th>
					<th>Vbody</th>
					<th>Idrain</th>
					<th>Igate</th>
					<th>Isource</th>
					<th>Ibody</th>
				</tr>''' )
		f2 = f.readlines()
		for i in range(len(f2)):
			f2[i] = f2[i].split()
			f1.write("<tr>")
			for j in range(len(f2[i])):
				f2[i][j] = f2[i][j][0:4] + f2[i][j][-5:-1] + f2[i][j][-1]

				f1.write("<td>"+f2[i][j]+"</td>")
			f1.write("</tr>")
		f1.write("</table> <br><br><br>")
		f.close()
f1.close()
